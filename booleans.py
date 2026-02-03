# x = True
# print(x)
# print(type(x))

def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >= 35

print("Can a 19-year-old run for president 1 ?", can_run_for_president(50)) # Returns True
print("Can a 45-year-old run for president 1 ?", can_run_for_president(25)) # Returns False

print("Can a 19-year-old run for president 2 ?", can_run_for_president(30)) # Returns False
print("Can a 45-year-old run for president 2 ?", can_run_for_president(40)) # Returns True

print("Can a 19-year-old run for president 3 ?", can_run_for_president(41)) # Returns True
print("Can a 45-year-old run for president 3 ?", can_run_for_president(51)) # Returns True

print("Can a 19-year-old run for president 4 ?", can_run_for_president(18)) # Returns False
print("Can a 45-year-old run for president 4 ?", can_run_for_president(20)) # Returns False