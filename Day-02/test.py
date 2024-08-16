arn = "aws:iam::123456789012:user/johndoe"
name = "jd"

print(arn.split("/"))
print(arn.split("/")[0])
print(arn.split("/")[1])

print(len(arn))

concat = name + "=" + arn

print(concat)