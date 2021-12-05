import numpy as np

def negamax(state, depth, role, alpha, beta):
    if game_over(state) or depth == 0:
        return state.score(role)