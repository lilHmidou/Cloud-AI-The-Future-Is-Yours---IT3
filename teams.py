class Team :
    def __init__ (self, name, trends, credits = 50):
        self.name = name
        self.trends = trends
        self.credits = credits
    
    def get_trends(self):
        return self.trends
    
    def get_credits(self):
        return self.credits
    
    def add_investment(self, amount):
        if amount > self.credits:
            raise ValueError("Investment exceeds available credits")
        self.credits -= amount
        print(f"Team {self.name} invested {amount} credits.")
        print(f"Team {self.name} has {self.credits} credits remaining.")
        return self.credits