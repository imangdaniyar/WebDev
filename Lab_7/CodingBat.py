#Warmup-1
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
def monkey_trouble(a_smile, b_smile):
  return not a_smile ^ b_smile
def sum_double(a, b):
  if a == b:
    return (a + b)*2
  return a + b
def diff21(n):
  if n > 21:
    return (n - 21)*2
  return 21 - n
def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)
def makes10(a, b):
  return a == 10 or b == 10 or a + b == 10
def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200 - n) <= 10 
def pos_neg(a, b, negative):
  return ((a > 0 and b < 0) or (a < 0 and b > 0)) and not negative or a < 0 and b < 0 and negative
def not_string(str):
  if not str.find('not'):
    return str
  return 'not ' + str
def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]
def front_back(str):
  if len(str) > 1:
    new = str[len(str)-1] + str[1:len(str) - 1] + str[0]
    return new
  else:
    return str
def front3(str):
  return str[:3]*3
#Warmup-2
def string_times(str, n):
  return str *n
def front_times(str, n):
  return str[:3]*n
def string_bits(str):
  new = ''
  for i in range(len(str)):
    if i % 2 == 0:
      new = new + str[i]
  return new
def last2(str):
  c = 0
  for i in range(len(str) - 2):
    if str[-2:] == str[i:i+2]:
     c += 1
  return c
def array_count9(nums):
  n = 0
  for i in nums:
    if i == 9:
      n +=1
  return n
def array_front9(nums):
  if len(nums) == 0:
    return False
  for i in range(len(nums)):
    if(i >= 4):  
      return False
    if nums[i] == 9:
        return True
    if i == len(nums) -1 :
      return False
def array123(nums):
  a = [1,2,3]
  check = []
  for j in a:
    for i in nums:
      if i == j:
        check.append(True)
        break
  if len(check) == 3:
    return True
  return False
def string_match(a, b):
  n = 0
  for i in range(len(a) - 1):
    for j in range(len(b) - 1):
      if a[i:i+2] == b[j:j+2] and i==j:
        n +=1
  return n
#String-1
def hello_name(name):
  return "Hello " + name + '!'
def make_abba(a, b):
  return a+b+b+a
def make_tags(tag, word):
  return '<' + tag + '>' + word + '</' + tag + '>'
def make_out_word(out, word):
  return out[:2] + word + out[2:]
def extra_end(str):
  return str[-2:]*3
def first_two(str):
  if len(str) > 2:
    return str[:2]
  return str
def first_half(str):
  return str[:len(str)/2]
def without_end(str):
  return str[1:-1]
def combo_string(a, b):
  if len(a) > len(b):
    return b+a+b
  return a+b+a
def non_start(a, b):
  return a[1:] + b[1:]
def left2(str):
  return str[2:] + str[:2]
#String-2
def double_char(str):
  result = ''
  for i in str:
    result += i*2
  return result
def count_hi(str):
  c = 0
  for i in range(len(str) - 1):
    if str[i:i+2] == 'hi':
      c +=1
  return c
def cat_dog(str):
  c = 0
  d = 0
  for i in range(len(str)):
    if str[i:i+3] == 'cat':
      c +=1
    if str[i:i+3] == 'dog':
      d +=1
  return d == c
def count_code(str):
  s = "code"
  c = 0
  for i in range(len(str)):
    for j in range(len(s)):
      if str[i] == s[j]:
        if i < len(str) - 1:
          i += 1  
      elif j == 2:
        if i < len(str) - 1:
          i += 1  
        continue
      else:
        break
      if j == 3:
        c += 1
  return c
def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())
def xyz_there(str):
  for i in range(len(str) - 2):
    if str[i] + str[i+1] + str[i+2] == "xyz" and (i == 0 or str[i-1] != '.'):
      return True
  return False
#List-1
def first_last6(nums):
  if len(nums) > 1:
    if nums[0] == 6 or nums[-1] == 6:
      return True
    else:
      return False
  if nums[0] == 6:
    return True
  else:
    return False
def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[-1]:
      return True
  return False
def make_pi():
  return [3,1,4]
def common_end(a, b):
  if a[-1] == b[-1] or a[0] == b[0]:
    return True
  return False
def sum3(nums):
  sum = 0
  for i in nums:
    sum+=i
  return sum
def rotate_left3(nums):
  nums.append(nums[0])
  return nums[1:]
def reverse3(nums):
  nums.reverse()
  return nums
def max_end3(nums):
  if nums[0]> nums[-1]:
    return [nums[0] for i in range(len(nums))]
  else:
    return [nums[-1] for i in range(len(nums))]
def sum2(nums):
  if len(nums) >= 2:
    return nums[1] + nums[0]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0
def middle_way(a, b):
  return [a[1],b[1]]
def make_ends(nums):
  return [nums[0],nums[-1]]
def has23(nums):
  return 2 in nums or 3 in nums
#List-2
def count_evens(nums):
  c = 0
  for i in nums:
    if i % 2 == 0:
      c += 1
  return c
def big_diff(nums):
  return max(nums) - min(nums)
def centered_average(nums):
  return (sum(nums) - min(nums) - max(nums))/(len(nums) - 2)
def sum13(nums):
  sum = 0
  check = False
  for i in range(len(nums)):
    if nums[i] == 13:
      check = True
      continue
    if not check:
      sum += nums[i]
    check = False
  return sum
def sum67(nums):
  check = False
  sum = 0
  for i in nums:
    if not check:
      if i == 6:
        check = True
        continue
      sum += i
    if i == 7:
      check = False
  return sum
def has22(nums):
  for i in range(len(nums) -1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  
  return False
#Logic-1
def cigar_party(cigars, is_weekend):
  if cigars >= 40:
    if not is_weekend:
      if cigars <= 60:
        return True
      else:
        return False
    return True
  return False
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1
def squirrel_play(temp, is_summer):
  if temp >= 60:
    if is_summer:
      if temp <= 100:
        return True
      else: 
        return False
    if temp <= 90:
      return True
    else:
      return False
  else:
    return False
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    if speed  > 65 and speed <= 85:
      return 1
    if speed > 85:
      return 2
  else:
    if speed <= 60:
      return 0
    if speed  > 60 and speed <= 80:
      return 1
    if speed > 80:
      return 2
def sorta_sum(a, b):
  if a + b >= 10 and a + b <= 19:
    return 20
  return a + b
def love6(a, b):
  return a == 6 or b == 6 or abs(a-b) == 6 or a + b == 6
def in1to10(n, outside_mode):
  if outside_mode:
    if n <=1 or n >= 10:
      return True
    return False
  if n >=1 and n <= 10:
    return True
  return False
def near_ten(num):
  if abs(round(float(num)/10)*10 - num) <= 2:
    return True
  return False
