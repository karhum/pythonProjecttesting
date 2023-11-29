# Application for web store

# base declaration
vip_points = 0
new_points = 0

# starting details
cost = float(input("Hello! Please type your sum in numbers. (€)\n"))
is_student = input("Are you a student? y/n\n").lower()
is_student = is_student[0] == "y"
is_vip = input("Do you have a VIP-account? y/n\n").lower()
is_vip = is_vip[0] == "y"

if is_vip:
    vip_points = int(input("How many points you have?\n"))

discount_code = input("Please type your discount code.\n")

# calculate with ONE discount code
if discount_code == "FALL23":
    cost = cost * 0.9
elif discount_code == "BK2SCHOOL" and is_student:
    cost = cost * 0.8

# calculate the VIP points and discount AFTER discount code
if is_vip:
    new_points = (cost // 10) * 100

    # the code for VIP - system
    total_vip = vip_points + new_points
    cost_reduction = total_vip // 1000 * 5
    cost -= cost_reduction
    # print(total_vip)
# check the total before adding shipment
# print(cost)

# add the shipment costs if < 99:
if cost < 99:
    cost += 7.95


print(f"Final sum is {cost} €")
