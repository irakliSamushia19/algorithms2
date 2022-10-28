def convert(income, income_type, whereto, limit):
    if isinstance(income, str) and len(income) <= limit:
        converted_num = 0
        if income_type == 'sm' and whereto == 'dec':
            daxvedra = income
            if len(income) < limit:
                daxvedra = str('0' * (limit - len(income)))
                daxvedra += income
            pow_sm = len(daxvedra) - 2
            for each in daxvedra[1: len(daxvedra)]:
                converted_num += int(each) * 2**pow_sm
                pow_sm -= 1
            if daxvedra[0] == '1':
                converted_num = -converted_num
        elif income_type == 'oc' and whereto == 'dec':
            daxvedra = income
            if len(income) < limit:
                daxvedra = str('0' * (limit - len(income)))
                daxvedra += income
            pow_sm = len(daxvedra) - 1
            for each in daxvedra:
                if daxvedra[0] == '0':
                    converted_num += int(each) * 2 ** pow_sm
                    pow_sm -= 1
                else:
                    if each == '1':
                        converted_num += 0
                        pow_sm -= 1
                    else:
                        converted_num += 1 * 2 ** pow_sm
                        pow_sm -= 1
            if daxvedra[0] == '1':
                converted_num = -converted_num
        elif income_type == 'tc' and whereto == 'dec':
            daxvedra = income
            if len(income) < limit:
                daxvedra = str('0' * (limit - len(income)))
                daxvedra += income
            pow_sm = len(daxvedra) - 1
            for each in daxvedra:
                if daxvedra[0] == '0':
                    converted_num += int(each) * 2 ** pow_sm
                    pow_sm -= 1
                else:
                    if each == '0':
                        converted_num += 1 * 2 ** pow_sm
                        pow_sm -= 1
                    else:
                        converted_num += 0 * 2 ** pow_sm
                        pow_sm -= 1
            if daxvedra[0] == '1':
                 converted_num = -converted_num - 1
        elif income_type == 'ex' and whereto == 'dec':
            daxvedra = income
            if len(income) < limit:
                daxvedra = str('0' * (limit - len(income)))
                daxvedra += income
            mid_num = (2**limit) // 2
            pow_sm = len(daxvedra) - 1
            for each in daxvedra:
                converted_num += int(each) * 2 ** pow_sm
                pow_sm -= 1
            converted_num = converted_num - mid_num
        elif income_type == 'bin' and whereto == 'dec':
            daxvedra = income
            if len(income) < limit:
                daxvedra = str('0' * (limit - len(income)))
                daxvedra += income
            pow_sm = len(daxvedra) - 1
            for each in daxvedra:
                converted_num += int(each) * 2 ** pow_sm
                pow_sm -= 1
        return f"{income} რიცხვი ათობითში არის  {converted_num}"
    if isinstance(income, int):
        converted_num = ''
        if income_type == 'dec' and whereto == 'sm':
            converting = ''
            hincome = income
            if income > 0:
                converted_num = '0'
            elif income < 0:
                income = -income
                converted_num = '1'
            while income != 0:
                converting += str(income % 2)
                income = income // 2
            if len(converting) + 1 < limit and income != 0:
                chasma = '0' * (limit - (len(converting) + 1))
                converted_num += chasma
            if len(converted_num + ('0' * (limit - len(converting) - 1)) + converting[::-1]) > limit:
                return 'ricxvi ar arsebobs'
            elif hincome == 0:
                return f"{'0' * limit} ან {'1' + '0' * (limit - 1)}"
            else:
                return f"{converted_num + ('0' * (limit - len(converting) - 1)) + converting[::-1]}"

        elif income_type == 'dec' and whereto == 'oc':
            umax = 2 ** limit // 2 - 1
            if income > 0 and income <= umax:
                while income != 0:
                    converted_num += str(income % 2)
                    income = income // 2
                return f"{'0' * (limit - len(converted_num)) + converted_num[::-1]}"
            elif income < 0 and income >= -umax:
                income = -income
                while income != 0:
                    if income % 2 == 0:
                        converted_num += '1'
                        income = income // 2
                    else:
                        converted_num += '0'
                        income = income // 2
                return f"{'1' * (limit-len(converted_num)) + converted_num[::-1]}"
            else:
                return f"{'1' * (limit-len(converted_num))} or {'0' * (limit-len(converted_num))}"

        elif income_type == 'dec' and whereto == 'tc':
            max_num = (2 ** limit) // 2 - 1
            if income > 0 and income <= max_num:
                while income != 0:
                    converted_num += str(income % 2)
                    income = income // 2
                return f"{'0' * (limit-len(converted_num)) + converted_num}"

            elif income < 0 and income >= -max_num - 1:
                income = -income - 1
                while income != 0:
                    if income % 2 == 0:
                        converted_num += '1'
                        income = income // 2
                    else:
                        converted_num += '0'
                        income = income // 2
                return f"{'1' * (limit-len(converted_num)) + converted_num[::-1]}"
            else:
                return f"{'0' * (limit - len(converted_num))}"
        
        elif income_type == 'dec' and whereto == 'ex':
            mid_num = 2 ** (limit - 1)
            if income >= 0:
                income = income + mid_num
                while income!= 0:
                    converted_num += str(income % 2)
                    income = income // 2
            elif income < 0:
                income = income + mid_num
                while income!= 0:
                    converted_num += str(income % 2)
                    income = income // 2
                          
            return f"{'0' * (limit - len(converted_num)) + converted_num[::-1]}"

print(convert(18, 'dec', 'tc', 8))






