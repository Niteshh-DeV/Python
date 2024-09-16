def product_except_self(nums):
    # Initialize the result array with 1's, which will store the prefix products first
    result = [1] * len(nums)

    # Calculate prefix products for each index
    prefix_product = 1
    for i in range(len(nums)):
        result[i] = prefix_product
        prefix_product *= nums[i]
    
    # Calculate suffix products and multiply with the prefix products
    suffix_product = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= nums[i]

    return result

nums =list(map(int ,input("Enter list:").split()))

print(product_except_self(nums))