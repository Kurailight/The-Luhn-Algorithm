# The-Luhn-Algorithm
1) Assign a weight to each digit, starting from the right, in sequence (e.g., 1, 2, 1, 2...)
2) Multiply the digits by their assigned weights. If the product is a two-digit number, sum its digits
3) Sum the resulting new sequence of digits (this is the check sum)
4) Check if the sum is divisible by 10. If it is, the provided credit card number is valid.
To determine the check digit, apply the above reasoning to a sequence of 15 digits.
