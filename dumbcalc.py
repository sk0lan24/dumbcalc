from colorama import Fore, Style
import pyfiglet

def calculate_final_score(high_score, num_tiers, decrease_factors, num_questions):
    total_penalty = sum(num_questions[i] * decrease_factors[i] for i in range(num_tiers))
    final_score = high_score - total_penalty
    return max(final_score, 0)

def calculate_dummy_coefficient(total_points_lost, high_score):
    return total_points_lost / high_score

def calculate_stupidity_level(final_score, high_score):
    percentage = (final_score / high_score) * 100
    if percentage >= 95:
         level_text = "Intelligent"
    elif percentage >= 85:
         level_text = "Probably Intelligent"
    elif percentage >= 78:
         level_text = "Average"
    elif percentage >= 55:
         level_text = "Half Retarded"
    else:
         level_text = "Fully Retarded"

    styled_text = pyfiglet.figlet_format(level_text,font= 'doom')
    return styled_text

def main():
    banner = pyfiglet.figlet_format('dumbCalc')
    print(Fore.GREEN + banner)
    
    high_score = float(input(Fore.RED + "Enter the highest possible score: "))
    num_tiers = int(input(Fore.GREEN + "Enter the number of tiers: "))
    decrease_factors = [float(input(Fore.MAGENTA + f"Enter the decrease factor for tier {i+1}: ")) for i in range(num_tiers)]
    num_questions = [0] * num_tiers

    total_questions = int(input(Fore.CYAN +"Enter the total number of questions asked: "))
    for i in range(total_questions):
        tier = int(input(Fore.WHITE + f"Enter the tier (1-{num_tiers}) of question {i+1}: "))
        num_questions[tier - 1] += 1

    final_score = calculate_final_score(high_score, num_tiers, decrease_factors, num_questions)
    total_points_lost = sum(num_questions[i] * decrease_factors[i] for i in range(num_tiers))
    dummy_coefficient = calculate_dummy_coefficient(total_points_lost, high_score)
    stupidity_level = calculate_stupidity_level(final_score, high_score)

    print()
    print(f"{Fore.BLUE}╔═ ◘ {Style.RESET_ALL}{Fore.BLUE}Final Score: {Style.RESET_ALL}{Fore.GREEN}{final_score:.1f}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}╠═══════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.BLUE}╠{Style.RESET_ALL}{Fore.YELLOW}══╗{Style.RESET_ALL}{Fore.YELLOW} ► Tier Penalties {Style.RESET_ALL}{Fore.BLUE}  ║{Style.RESET_ALL}")
    for i, penalty in enumerate(decrease_factors):
        print(f"{Fore.BLUE}║{Style.RESET_ALL}{Fore.YELLOW}  ╟─── {Style.RESET_ALL}{Fore.CYAN}Tier{i+1}: {Style.RESET_ALL}{Fore.RED}{penalty:.1f} pts  {Style.RESET_ALL}{Fore.BLUE}║{Style.RESET_ALL}")
    print(f"{Fore.BLUE}╠══╩════════════════════╝{Style.RESET_ALL}")
    print(f"{Fore.BLUE}╠══ {Style.RESET_ALL}{Fore.RED}♥ {Style.RESET_ALL}{Fore.GREEN}Stupidity Coefficient: {Style.RESET_ALL}{Fore.RED}{dummy_coefficient:.2f}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}╚══ {Style.RESET_ALL}{Fore.YELLOW}☻ {Style.RESET_ALL}{Fore.GREEN}Stupidity Level: {Style.RESET_ALL}")
    print(f"{Fore.RED}{stupidity_level}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
