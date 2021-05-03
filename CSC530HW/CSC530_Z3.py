#Author: Ziwei Wu
from z3 import Implies, Int, And, Or, solve, eq, substitute, Ints, IntVal

#Notes: substitute(e, [(a,b)]) ==> replace 'a' with 'b' in expression e
# substitute(e,[(a,z3.IntVal(3))]) ==> replace 'a' in expression e with the number 3
#x, y, z = Ints('x y z')

a1, a2, a3, a4, a5, a6, x, y = Ints('a1 a2 a3 a4 a5 a6 x y')

#The example function that was used in the paper
pv1 = """
PV1 (int y) {
    x := −50;
    while (x < 0) {
        x := x + y;
        y++;
    }
    assert(y > 0)
}
"""

#assuming we parse it and got the constraints...
#===========================================================================================
#This section is for the Constraint Solving Section of the paper (Section 2.2)
#the invariant template given in the paper
# invariant_template = Or(a1*x + a2*y + a3 >= 0, a4*x + a5*y + a6 >= 0) # a1x + a2y + a3 ≥ 0 ∨ a4x + a5y + a6 ≥ 0

#the first constraint is the entry constraint, x := -50;
# true ⇒ (−50a1 + a2y + a3 ≥ 0) ∨ (−50a4 + a5y + a6 ≥ 0)

# true ⇒ e1 ≥ 0 ∨ e2 ≥ 0, where e1 ≡ −50a1 +a2y +a3 ≥ 0 and e2 ≡ −50a4 + a5y + a6 ≥ 0

# ¬((−e1 −1 ≥ 0) ∧ (−e2 − 1 ≥ 0))

# ∃λ1, λ2 ≥ 0, λ > 0(∀x,yλ1(−e1−1)+λ2(−e2−1) ≡ −λ).

#The L's represent the lambda symbols
L = Int('L')
L1 = Int('L1')
L2 = Int('L2')

#after applying Farkas' lemma, we get (for the first constraint)
fc_1 = (50*a1*L1 - a3 *L1 - L1) + (50*a4*L2 - a6 *L2 - L2 ) == -L #(50a1λ1 − a3λ1 − λ1) + (50a4λ2 − a6λ2 − λ2) = −λ 
fc_2 = a2*L1 + a5*L2 == IntVal(0) #a2λ1 + a5λ2 = 0
solve(fc_1, fc_2) #we take the two equations and then solve them

#The answer:
# [a3 = -36,
#  a6 = 38,
#  a4 = 20,
#  a2 = 0,
#  a5 = 0,
#  L = 3,
#  a1 = 0,
#  L2 = 2,
#  L1 = -55]

#Any solution is proof of correctness
#==========================================================================================

#==========================================================================================
# This section demonstrates the loop header's constraint of the first function
# I.e., I ∧ x < 0 ⇒ I[(y+1)/y, (x+y)/x]
# I = (x <0 ∨ y > 0)

# Substituting 'I' gives us:
# (x < 0 ∨ y > 0) ∧ x < 0 ⇒ (x <0 ∨ y > 0)[(y+1)/y, (x+y)/x]

#Reduce it
# x < 0 ⇒ (x+y <0 ∨ y+1 > 0)

#Using or-and-if to expand the implications gives us:
# ¬(x < 0) ∨ (x+y <0 ∨ y+1 > 0)

#Into the following:
# x >= 0 ∨ (x+y <0 ∨ y+1 > 0)

#How to we make (x+y <0 ∨ y+1 > 0) into "Something >= 0"?

#Apply Farkas's Lemma

#Get Constraints

#Solve via Z3

#==========================================================================================