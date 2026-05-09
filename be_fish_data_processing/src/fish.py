from dataclasses import dataclass

@dataclass
class Fish:
    rarity: str
    level: str
    growth: float
    speed: float
    adj_speed: float
    odds: int
    xp: float
    loot_efficiency: float
    type: str
    amount: int
    have: bool
    projected_amount: int
    
    def set_amount(self, value: int):
        self.amount = value
    def set_have(self, value: bool):
        self.have = value
    def to_dict(self):
        return {
            "type": self.type,
            "rarity": self.rarity,
            "level": self.level,
            "growth": self.growth,
            "speed": self.speed,
            "adj_speed": self.adj_speed,
            "odds": self.odds,
            "xp": self.xp,
            "loot_efficiency": self.loot_efficiency,
            "amount": self.amount,
            "have": self.have,
            "projected_amount": self.projected_amount
        }