SendMode, Input
SetBatchLines, -1

; ==================================================
; USER SETTINGS
; ==================================================

speed := 1.879
rows := 8

; base timing model
baseTime := 54000 / speed
rowTime := baseTime * 1.02
returnTime := baseTime * 1.02
rowShiftTime := (baseTime / rows) * 1.13

; safety / correction
wallPush := 500
step := 10

; anchor tuning
anchorDownTime := 500
anchorLeftTime := 1000
anchorExtraPush := 500

toggle := false

; ==================================================
; TOGGLE
; ==================================================

F2::
toggle := !toggle

if (toggle) {
    ToolTip, RUNNING (Stable Sweep)
    SoundBeep, 1000, 150
    SetTimer, MainLoop, 10
} else {
    ToolTip, STOPPED
    SoundBeep, 500, 150
    SetTimer, MainLoop, Off
    SendInput, {w up}{a up}{s up}{d up}
}
return

; ==================================================
; MAIN LOOP
; ==================================================

MainLoop:
SetTimer, MainLoop, Off

while (toggle)
{
    FullReset()
    Sweep()
    ReturnToStart()
}
return

; ==================================================
; CORNER ANCHOR (BOTTOM-LEFT FIX)
; ==================================================

FullReset() {
    global toggle, anchorDownTime, anchorLeftTime, anchorExtraPush

    ToolTip, Anchoring bottom-left...

    ; ALWAYS clear stuck inputs first
    SendInput, {w up}{a up}{s up}{d up}
    Sleep, 100

    ; force bottom boundary
    HoldKey("s", anchorDownTime)

    ; force left boundary
    HoldKey("a", anchorLeftTime)

    ; extra corner guarantee
    HoldKey("a", anchorExtraPush)
    HoldKey("s", anchorExtraPush)

    ; release before starting movement
    SendInput, {a up}{s up}{d up}{w up}
    Sleep, 100
}

; ==================================================
; SWEEP (FIXED DIRECTION LOGIC)
; ==================================================

Sweep() {
    global toggle, rows, rowTime, rowShiftTime, wallPush

    direction := 1  ; 1 = right, -1 = left

    Loop, %rows%
    {
        if (!toggle)
            return

        ; -------------------------
        ; horizontal movement
        ; -------------------------
        if (direction = 1)
        {
            HoldKey("d", rowTime)
            HoldKey("d", wallPush)  ; force right wall
        }
        else
        {
            HoldKey("a", rowTime)
            HoldKey("a", wallPush)  ; force left wall
        }

        ; -------------------------
        ; vertical step
        ; -------------------------
        if (A_Index < rows)
            HoldKey("w", rowShiftTime)

        ; flip direction manually (NO A_Index dependency)
        direction *= -1
    }

    ToolTip, Top reached
}

; ==================================================
; RETURN TO START
; ==================================================

ReturnToStart() {
    global toggle, returnTime

    ToolTip, Returning...

    HoldKey("s", returnTime)
}

; ==================================================
; TIME-ROBUST HOLD FUNCTION
; ==================================================

HoldKey(key, duration) {
    global toggle, step

    SendInput, {%key% down}

    start := A_TickCount

    while (toggle && (A_TickCount - start < duration))
    {
        Sleep, step
    }

    SendInput, {%key% up}
}