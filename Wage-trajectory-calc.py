import sys
import datetime

# The Incorruptible Ledger Suite: Macroeconomic Stagnation Module
# Tracks nominal wage trajectory vs True Cost of Living (CPI) and Fiscal Drag since 2000

def calculate_real_wage_theft(nominal_wage_today):
    print("Executing historical wage trajectory audit (2000 - 2026)...")
    
    # Historical Baseline Metrics (UK Office for National Statistics & HMRC Archives)
    avg_wage_2000 = 18800.00
    personal_allowance_2000 = 4385.00
    
    # Cumulative true asset and living cost inflation (housing, food, energy) since 2000 is ~105%
    true_inflation_multiplier = 2.05 
    
    # 1. Calculate what a baseline wage from 2000 SHOULD be today to maintain purchasing power
    target_real_wage_today = avg_wage_2000 * true_inflation_multiplier
    
    # 2. Calculate the "Trapped Income Gap" (The Stagnation Vector)
    trajectory_loss_gbp = target_real_wage_today - nominal_wage_today
    percentage_loss = (trajectory_loss_gbp / target_real_wage_today) * 100
    
    # 3. Fiscal Drag Auditing (Threshold Freeze Impact Extended to 2030)
    frozen_allowance_today = 12570.00
    fair_allowance_today = personal_allowance_2000 * true_inflation_multiplier
    hidden_taxable_exposure = fair_allowance_today - frozen_allowance_today
    
    # Standard 20% basic tax rate theft due to frozen threshold
    annual_fiscal_drag_theft = hidden_taxable_exposure * 0.20
    
    # Projected cumulative theft from threshold freeze extension (2026 to 2030 freeze block)
    projected_theft_to_2030 = annual_fiscal_drag_theft * 4
    
    print("\n================ FORENSIC ECONOMIC AUDIT OUTCOME ================")
    print(f"Target Wage required to match year 2000 purchasing weight:  £{target_real_wage_today:,.2f}")
    print(f"Your Actual Nominal Wage entered:                           £{nominal_wage_today:,.2f}")
    print(f"Total Lifetime Purchasing Power Drained from your Pocket:   £{trajectory_loss_gbp:,.2f}")
    print(f"Mathematical Loss in your Personal Wage Trajectory:         {percentage_loss:.1f}%")
    print(f"\n[FISCAL DRAG EXPOSURE - FREEZE EXTENDED TO 2030]")
    print(f"Fair Tax-Free Threshold if indexed to real costs:           £{fair_allowance_today:,.2f}")
    print(f"Government Frozen Threshold today:                          £{frozen_allowance_today:,.2f}")
    print(f"Annual Stealth Tax Stolen by the State via Threshold Freeze:  £{annual_fiscal_drag_theft:,.2f}")
    print(f"Projected Cumulative Stealth Tax Stolen from 2026 to 2030:  £{projected_theft_to_2030:,.2f}")
    print("=================================================================\n")

# Processed full-time UK National Minimum Wage (National Living Wage) baseline for 2026
calculate_real_wage_theft(23809.00)

