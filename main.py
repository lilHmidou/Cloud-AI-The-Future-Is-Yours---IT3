import time
from teams import Team
from ai_events import what_is_the_trend, twist_event, random_event, apply_twist, convert_trend_choice,convert_investment_choice
import random


def main():
    print("Welcome to the AI in Cloud Strategy Game!")
    print("---------------------------------------------")
    print ("Teams, please choose your team name and the two trends you believe \n will have the most impact on cloud computing in the next 5 years.")
    print("---------------------------------------------") 
    print ("Available Trends:\n" \
    "1. Rise of Agentic AI Systems\n" \
    "2. Distributed & Hybrid AI Architectures\n" \
    "3.Integration of Quantum Computing\n" \
    "4.Infrastructure & Compute Diversification\n" \
    "5.Green AI\n" \
    "6.AI-Specific Governance & Security\n")
    print("---------------------------------------------")
    input_name = input("Enter your Team Name: ")
    trend1_input = input("First Trend Choice (choose the number affiliate): ")
    trend2_input = input("Second Trend Choice (choose the number affiliate): ")
    trends = [convert_trend_choice(trend1_input), convert_trend_choice(trend2_input)]
    
    team = Team(input_name, trends)
    print(f"Team {team.name} has chosen the trends: {', '.join(team.trends)}")
    print("---------------------------------------------")
    for trend in team.trends:
        print(f"Trend: {trend}")
        print(what_is_the_trend(trend))
        print("---------------------------------------------")
    input("Press Enter to proceed to the Investment Phase... are you ready ?")
    print("---------------------------------------------")
    print("Each team starts with 50 Cloud Credits to invest in strategic areas. (each cost is random between 10 and 25 credits)")
    print("Available Investment Areas: \n" \
    "1. Scalability\n"
    "2. Cost_reduction\n"
    "3. AI_ethics\n"
    "4. Model_performance\n"
    "5. Accessibility\n")
    time.sleep(10)
    print("---------------------------------------------")
    print("Please allocate your investments (only 2 areas allowed). " \
    "Choose the number affiliate \n" \
    "( 1 = Scalability,\n 2 = Cost_reduction,\n 3 = AI_ethics,\n 4 = Model_performance,\n 5 = Accessibility,\n)")
    print("---------------------------------------------")
    investements1_input = input("First Investment Area: ")
    investements1 = convert_investment_choice(investements1_input)
    investements2_input = input("Second Investment Area: ")
    investements2 = convert_investment_choice(investements2_input)
    investments = {investements1: random.randint(10, 25), investements2: random.randint(10, 25)}
    team.add_investment(investments.get(investements1))
    team.add_investment(investments.get(investements2))
    print(f"Team {team.name} has invested in: {investements1} and {investements2}")
    print("---------------------------------------------")
    time.sleep(10)
    event = random_event()
    print(f"A new market event has occurred: {event}")
    impact_message = apply_twist(team, event)
    print(impact_message)
    print("---------------------------------------------")
    print(f"Team {team.name} now has {team.get_credits()} Cloud Credits remaining.")
    print("Thank you for playing the AI in Cloud Strategy Game!")

if __name__ == "__main__":
    main() 

