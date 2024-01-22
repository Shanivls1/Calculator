import pytest
from src.solver import solve


def solve_response(expression):
    try:
        res = solve(expression)
        return res
    except Exception:
        return "err"


def test_solver():
    #syntax error:
    assert solve_response("3^*4") == "err"
    assert solve_response("0+(-)4") == "err"
    assert solve_response("~-~2@!3") == "err"
    assert solve_response("8345.46.342-4!") == "err"
    assert solve_response("-(4325+3") == "err"

    assert solve_response("kqfjo=2-fdksja4") == "err"
    assert solve_response("") == 0
    assert solve_response(" ") == 0

    # simple expressions
    assert solve_response(".5/2+5") == 5.25
    assert solve_response("5%3&4") == 2.0
    assert solve_response("4@7*2") == 11.0
    assert solve_response("4$5%4") == 1.0
    assert solve_response("1235.01/1.4#@4") == 274.44666667
    assert solve_response("0.001$0.002") == 0.002
    assert solve_response("3!!") == 720.0
    assert solve_response("5+4!+235#") == 39.0
    assert solve_response("2+3%7&5-8") == -3.0
    assert solve_response("1+3@7&6-2") == 4.0
    assert solve_response("9@7%4-2^5") == -32.0
    assert solve_response("8$7%3-5^2") == -23.0
    assert solve_response("1+3@7&6-2") == 4.0

    # advanced expression
    assert solve_response("(5*3)#$3@(4!@45#)#") == 9.0
    assert solve_response("9$2+(5-4)^3.2/((2.7&1.8)@3.6)") == 9.37037037
    assert solve_response("((2+3)@4-5*6^2%3)$7+(8&9)") == 15.0
    assert solve_response("(4*(7%3$2)-~-1)^(3&5)") == 27.0
    assert solve_response("2+(6*4^3)%5-9@((1+7)@4)") == -1.5
    assert solve_response("((2.5+3)@4.8-5*6^2%3)$7.3+(8.6&9)") == 15.9
    assert solve_response("4-3+(4234.5&34)+4^(4)-23") == 268.0
    assert solve_response("((2.8+34.5%7.4)&(5.6-8))@(9.1%4.3)") == -0.95
    assert solve_response("5.2@(9/3.7%4)&7.9+((2^3)@1.4)") == 8.51621622
    assert solve_response("4.6+6*(2/~-3)%1@(5.26-7.8)") == 3.98000002
    assert solve_response("534263.4-(4.2^(3%2.5243))$7@(1.9+9.3)") == 534254.3
    assert solve_response("9.6$2+(5.7-4)^3.9/((2.5&1.7)@3.8)") == 12.48016985
    assert solve_response("8.4$(7%(3.6-5))^2.3+(1.5^4.2)") == 139.10118249
    assert solve_response("((2.3+9.7@(1.4*6.5))-4.1)@(3.8+7.2)") == 9.3
    assert solve_response("(6.9+(4.1$2.6-1.7)&3.4^2.8)@9.5-(8.7^4.3)") == -10949.08334136
    assert solve_response("6.4*(2.7@(4.5-1%~-3.8))+(5.9&7.1)") == 25.74
    assert solve_response("((2.8+9.5@(1.6*6.2))-4.3)@(3.7+7.4)") == 9.655
    assert solve_response("(4.8*(7.2%3.6+2.9)#+~-1.4)^(3.5&5.7)") == 1172188.62565367
    assert solve_response("((2.3+3.7)@4.9-5.1*6.3^2%3.2)$7.6+(8.9&9.4)") == 16.5
    assert solve_response("5.8@(9.3/3.7%4.6)&7.2+((2.7^3.5)@1.8)") == 21.22799141
