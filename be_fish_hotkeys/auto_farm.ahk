toggle := false

F1::
toggle := !toggle

if (toggle) {
    SetTimer, PressW, 180000   ; 3 minutes
    SetTimer, ClickRoutine, 180000  ; 3 minutes

    ToolTip, Script ON (W every 3 min + double click every 1 min)
    SoundBeep, 1000, 150

    Gosub, PressW
    Gosub, ClickRoutine
} else {
    SetTimer, PressW, Off
    SetTimer, ClickRoutine, Off

    ToolTip, Script OFF
    SoundBeep, 500, 150
    SetTimer, RemoveToolTip, 2000
}
return

; -------------------
; HOLD W (3 min cycle)
; -------------------
PressW:
ToolTip, Holding W...

SendInput, {w down}
Sleep, 2000
SendInput, {w up}

SetTimer, RemoveToolTip, 2000
return

; -------------------
; CLICK → WAIT → CLICK (1 min cycle)
; -------------------
ClickRoutine:
ToolTip, Clicking...

Click
Sleep, 2000
Click

SetTimer, RemoveToolTip, 2000
return

; -------------------
; TOOLTIP CLEAR
; -------------------
RemoveToolTip:
ToolTip
return