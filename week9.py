print("Sanath S Shetty")
print("1BM23CS297")

# a. ¬food(x) V likes(John, x)
clause_a = {"NOT food(x)", "likes(John, x)"}
# d. ¬eats(y, z) V killed(y) V food(z)
clause_d = {"NOT eats(y, z)", "killed(y)", "food(z)"}
# e. eats(Anil, Peanuts)
clause_e = {"eats(Anil, Peanuts)"}
# f. alive(Anil)
clause_f = {"alive(Anil)"}
# g. ¬eats(Anil, w) V eats(Harry, w)
clause_g = {"NOT eats(Anil, w)", "eats(Harry, w)"}
# h. killed(g) V alive(g)
clause_h = {"killed(g)", "alive(g)"}
# i. ¬alive(k) V ¬killed(k)
clause_i = {"NOT alive(k)", "NOT killed(k)"}

# ----------------------------------------------------------------
# Step 2: Add the Negated Goal
# ----------------------------------------------------------------
# The goal is "likes(John, Peanuts)"[cite: 141, 163].
# The negated goal is "¬likes(John, Peanuts)"[cite: 259].
negated_goal = {"NOT likes(John, Peanuts)"}


# ----------------------------------------------------------------
# Step 3: Perform the Resolution (Refutation)
# ----------------------------------------------------------------
# This function simulates the resolution process.
def resolve(clause1, literal1, clause2, literal2):
    """
    A simple function to simulate resolving two clauses
    where literal1 and literal2 are the complementary literals.
    e.g., literal1 = "food(x)", literal2 = "NOT food(x)"
    """
    # Create copies to avoid modifying the originals
    new_clause = clause1.union(clause2)
    # Remove the two complementary literals
    new_clause.remove(literal1)
    new_clause.remove(literal2)
    return new_clause

print("Starting Resolution Proof...\n")
print(f"Goal: Prove 'likes(John, Peanuts)'")
print(f"Negated Goal: {negated_goal}\n")

# --- Proof Step 1 ---
# Resolving:
#   {NOT likes(John, Peanuts)}  (Negated Goal)
#   {NOT food(x), likes(John, x)}  (Clause a)
# Unification: {x / Peanuts}
# Result: {NOT food(Peanuts)}
print("Step 1: Resolving Negated Goal with Clause a")
print(f"  {negated_goal}")
print(f"  {clause_a}  [Unify x=Peanuts]")
resolvent_1 = resolve(negated_goal, "NOT likes(John, Peanuts)",
                      clause_a, "likes(John, x)")
# Manually apply unification
resolvent_1.remove("NOT food(x)")
resolvent_1.add("NOT food(Peanuts)")
print(f"  Result 1: {resolvent_1}\n")

# --- Proof Step 2 ---
# Resolving:
#   {NOT food(Peanuts)}  (Result 1)
#   {NOT eats(y, z), killed(y), food(z)} (Clause d)
# Unification: {z / Peanuts}
# Result: {NOT eats(y, Peanuts), killed(y)}
print("Step 2: Resolving Result 1 with Clause d")
print(f"  {resolvent_1}")
print(f"  {clause_d}  [Unify z=Peanuts]")
resolvent_2 = resolve(resolvent_1, "NOT food(Peanuts)",
                      clause_d, "food(z)")
# Manually apply unification
resolvent_2.remove("NOT eats(y, z)")
resolvent_2.remove("killed(y)")
resolvent_2.add("NOT eats(y, Peanuts)")
resolvent_2.add("killed(y)")
print(f"  Result 2: {resolvent_2}\n")

# --- Proof Step 3 ---
# Resolving:
#   {NOT eats(y, Peanuts), killed(y)} (Result 2)
#   {eats(Anil, Peanuts)} (Clause e)
# Unification: {y / Anil}
# Result: {killed(Anil)}
print("Step 3: Resolving Result 2 with Clause e")
print(f"  {resolvent_2}")
print(f"  {clause_e}  [Unify y=Anil]")
resolvent_3 = resolve(resolvent_2, "NOT eats(y, Peanuts)",
                      clause_e, "eats(Anil, Peanuts)")
# Manually apply unification
resolvent_3.remove("killed(y)")
resolvent_3.add("killed(Anil)")
print(f"  Result 3: {resolvent_3}\n")

# --- Proof Step 4 ---
# Resolving:
#   {killed(Anil)} (Result 3)
#   {NOT alive(k), NOT killed(k)} (Clause i)
# Unification: {k / Anil}
# Result: {NOT alive(Anil)}
print("Step 4: Resolving Result 3 with Clause i")
print(f"  {resolvent_3}")
print(f"  {clause_i}  [Unify k=Anil]")
resolvent_4 = resolve(resolvent_3, "killed(Anil)",
                      clause_i, "NOT killed(k)")
# Manually apply unification
resolvent_4.remove("NOT alive(k)")
resolvent_4.add("NOT alive(Anil)")
print(f"  Result 4: {resolvent_4}\n")

# --- Proof Step 5 ---
# Resolving:
#   {NOT alive(Anil)} (Result 4)
#   {alive(Anil)} (Clause f)
# Unification: {}
# Result: {} (Empty Clause)
print("Step 5: Resolving Result 4 with Clause f")
print(f"  {resolvent_4}")
print(f"  {clause_f}")
resolvent_5 = resolve(resolvent_4, "NOT alive(Anil)",
                      clause_f, "alive(Anil)")
print(f"  Result 5: {resolvent_5}\n")

# --- Conclusion ---
if not resolvent_5: # Check if the set is empty
    print("--------------------------------------------------")
    print("Conclusion: An empty clause {} was derived.")
    print("This is a contradiction, which means the negated goal is false.")
    print("Therefore, the original goal 'likes(John, Peanuts)' is TRUE.")
    print("Hence proved. ")
else:
    print("Proof failed. Could not derive the empty clause.")