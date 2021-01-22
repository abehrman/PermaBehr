import black_scholes_merton as bsm

def test_price_ex1():
    # https://medium.com/magnimetrics/black-scholes-model-first-steps-bdcbe1691da7

    spot = 60
    exercise = 58
    rate = .035
    time = .5
    div_rate = .0125
    sigma = .2

    myOption = bsm.BSMoption(
        spot, exercise, sigma, time, rate, div_rate)
    

    d1 = myOption._d1(spot, time)
    d2 = myOption._d2(spot, time)

    assert round(d1, 4) == .39
    assert round(d2, 4) ==  .2486

    assert round(myOption.black_scholes_call(),2) == 4.77

    assert round(myOption.black_scholes_put(), 2) == 2.14
        
    return None

def test_price_ex2():
    # https://www.erieri.com/blackscholes

    spot = 25
    exercise = 15
    rate = .05
    time = 3.5
    div_rate = .0
    sigma = .2

    myOption = bsm.BSMoption(
        spot, exercise, sigma, time, rate, div_rate)
    

    d1 = myOption._d1(spot, time)
    d2 = myOption._d2(spot, time)

    assert round(myOption.black_scholes_call(),4) == 12.4942

    assert round(myOption.black_scholes_put(), 3) == 0.086
        
    return None