# program-analysis-using-constraints-ziweiwu

* I tried to use the Python Z3 library, but it didn't work, so I downloaded the Z3 Github repository and built it. 
* I may have accidentally uploaded the Z3 Github repo and I'm too afraid to touch it for fear of something breaking.
* The CSC530HW folder contains the CSC530_Z3.py file, which contains what I did.

This is what I did in my 3 to 4 hours:
* I read the paper and tried to understand how something like this would be implemented
* I played around with Z3 and learned how to use it
* I followed around with the example of constraint solving that the paper gives (Section 2.2).
* I tried to apply the same thing, but with the loop header constraint (I ∧ x < 0 ⇒ I[(y+1)/y, (x+y)/x]), where I = (x <0 ∨ y > 0).
* I got as far as:

-----------------------------------
Substituting 'I' gives us:  
(x < 0 ∨ y > 0) ∧ x < 0 ⇒ (x <0 ∨ y > 0)[(y+1)/y, (x+y)/x]

Reduce it  
x < 0 ⇒ (x+y <0 ∨ y+1 > 0)

Using or-and-if to expand the implications gives us:  
¬(x < 0) ∨ (x+y <0 ∨ y+1 > 0)

Into the following:  
x >= 0 ∨ (x+y <0 ∨ y+1 > 0)

--------------------------------------

And then I got stuck on what to do next for half an hour before I gave up.  
I tried to look up logic on Wikipedia to try to figure out how to turn it all into ORs with "... >= 0" so that I could use Farkas' Lemma on it.  

# The section below is my second attempt at figuring out the loop header constraint, but with I as the invariant template the paper used
---------------------------------
I = a1x + a2y + a3 ≥ 0 ∨ a4x + a5y + a6 ≥ 0

I ∧ x < 0 ⇒ I[(y+1)/y, (x+y)/x]

= ¬(I ∧ x < 0) ∨ I[(y+1)/y, (x+y)/x]

=  (¬I ∨ ¬(x < 0)) ∨ I[(y+1)/y, (x+y)/x]

= (¬I ∨ x >= 0) ∨ I[(y+1)/y, (x+y)/x]

= ((e1 < 0 ∧ e2 < 0) ∨ x >= 0) ∨ (e3 >= 0 ∨ e4 >= 0), where e1 = a1x + a2y + a3 and e2 = a4x + a5y + a6; e3 and e4 are e1 and e2 with the x and y substituted.

And like my first attempt, I am also stuck in this area of figuring out what the next step would be to turn this into something that Farkas' Lemma can be applied to.
