def main():
  name = input("Enter employee's name:")
  num_hour = int(input("Enter number of hours worked in a week:"))
  rate = float(round(input("Enter hourly pay rate:"), 1))
  f_tax = float(input("Enter federal tax withholding rate:"))
  s_tax = float(input("Enter state tax withholding rate:"))
  g_pay = num_hour *rate
  
  f_tax = round(g_pay * .2, 2)
  s_tax = round(g_pay * .09, 2)
  t_tax = (f_tax + s_tax)

  print("Employee Name:", name)
  print("Hours Worked:", num_hour)
  print("Pay Rate:", rate)
  print("Gross Pay:", g_pay)
  print("Deductions:")
  print("  Federal Withholding (20.0%):", f_tax)
  print("  State Withholding (9.0%):", s_tax)
  print("  Total Deduction:", t_tax)
  print("Net Pay:", g_pay - t_tax) 

main()