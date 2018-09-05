def mergingVines(vines, n):
    def nTimes(n):
        def real_decorator(func):
            def wrapper(vines):
                v = vines
                for i in range(n):
                    v = func(v)
                return v
            return wrapper
        return real_decorator

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)

def test():
    testeql(mergingVines([1,2,3,4,5], 2), [10,5])
