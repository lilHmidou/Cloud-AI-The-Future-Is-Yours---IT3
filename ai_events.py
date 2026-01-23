from teams import Team
import random

def what_is_the_trend(trend):
    trends_info = {
        "Rise of Agentic AI Systems": "AI that acts semi-autonomously to execute multi-step workflows,\n moving beyond simple prompts to manage entire business processes",
        "Distributed & Hybrid AI Architectures": "Processing AI workloads across centralized clouds, regional hubs,\n and local edge devices to optimize for data sovereignty, latency, and energy use",
        "Integration of Quantum Computing": "Using  as specialized accelerators within hybrid classical-quantum workflows to solve complex optimization\n and simulation problems intractable for classical systems",
        "Infrastructure & Compute Diversification": "Moving beyond a sole reliance on Nvidia GPUs to include diverse chips (e.g., Google TPUs, AWS Trainium),\n ARM-based processors, and specialized GPU cloud providers",
        "Green AI": "Green AI focuses on developing energy-efficient algorithms \nand models to minimize the environmental impact of AI technologies, promoting sustainability in cloud computing.",
        "AI-Specific Governance & Security": "AI Governance and Regulation are critical \n for ensuring ethical use of AI, addressing biases, and complying with legal standards, which will shape the future landscape of AI in cloud."
    }
    return trends_info.get(trend, "Trend information not available.")

def twist_event(event):
    events_info = {
        "Strict regulation on AI": 1,
        "Explosion in cloud costs": 2,
        "Breakthrough open-source": 3,
        "Environmental constraints": 4
    }
    return events_info.get(event, "Event information not available.")

def convert_trend_choice(choice):
    trend_mapping = {
        "1": "Rise of Agentic AI Systems",
        "2": "Distributed & Hybrid AI Architectures",
        "3": "Integration of Quantum Computing",
        "4": "Infrastructure & Compute Diversification",
        "5": "Green AI",
        "6": "AI-Specific Governance & Security"
    }
    return trend_mapping.get(choice, "Invalid choice")

def convert_investment_choice(choice):
    investment_mapping = {
        "1": "Scalability",
        "2": "Cost reduction",
        "3": "AI ethics & Security",
        "4": "Model performance",
        "5": "Accessibility (no-code, APIs)"
    }
    return investment_mapping.get(choice, "Invalid choice")

def random_event():
    events = [
        "Strict regulation on AI",
        "Explosion in cloud costs",
        "Breakthrough open-source",
        "Environmental constraints"
    ]
    return random.choice(events) 


def apply_twist(team, event):
    impact = twist_event(event)
    if impact == "Event information not available.":
        return "No significant impact on strategy."
    if impact == 1 :
        team.credits -= random.randint(0, 35)  
        return f"Team {team.name} loses 5 credits due to strict AI regulations."
    if impact == 2 :
        team.credits -= random.randint(0, 90) 
        return f"Team {team.name} loses 10 credits due to increased cloud costs."
    if impact == 3 :
        team.credits += random.randint(0, 70)  
        return f"Team {team.name} gains 15 credits from open-source breakthroughs."
    if impact == 4 :
        team.credits -= random.randint(0, 50) 
        return f"Team {team.name} loses 20 credits due to environmental constraints."