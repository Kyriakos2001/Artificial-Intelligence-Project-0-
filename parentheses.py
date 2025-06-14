def complete_parentheses(expr):

    stack = []

    # Ορισμός των τελεστών που υποστηρίζονται
    operators = {'+', '-', '*', '/', '–'}
    for token in expr:
        
        # Εάν το τρέχον token δεν είναι ')', γίνεται πρόσθεση του token στη στοίβα
        if token != ')':
            stack.append(token)

        else:
            
            # Ανάκτηση του δεύτερου τελεστή από τη στοίβα
            operand2 = stack.pop()
            
            # Ανάκτηση του τελεστή από τη στοίβα
            operator = stack.pop()

            # Ανάκτηση του πρώτου τελεστή από τη στοίβα
            operand1 = stack.pop()
            
            # Δημιουργία νέας έκφρασης
            new_expr = ['(']
            
            # Εάν ο πρώτος τελεστής είναι λίστα, γίνετε πρόσθεση των στοιχείων του
            if isinstance(operand1, list):
                new_expr.extend(operand1)

            # Εάν ο πρώτος τελεστής είναι χαρακτήρας, γίνετε πρόσθεση του χαρακτήρα
            else:
                new_expr.append(operand1)
            new_expr.append(operator)

            # Εάν ο δεύτερος τελεστής είναι λίστα, γίνετε πρόσθεση των στοιχείων του
            if isinstance(operand2, list):
                new_expr.extend(operand2)

            # Εάν ο δεύτερος τελεστής είναι χαρακτήρας, γίνετε πρόσθεση του χαρακτήρα
            else:
                new_expr.append(operand2)
            new_expr.append(')')
            stack.append(new_expr)

    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item
    return list(flatten(stack))

# Ζητάμε από τον χρήστη να εισάγει την αριθμητική παράσταση
user_input = input("Εισάγετε την αριθμητική παράσταση: ")

# Μετατροπή της εισόδου σε λίστα
expr = user_input.strip().split()

# Κάλεσμα της συνάρτησης με την είσοδο του χρήστη
result = complete_parentheses(expr)

# Εκτύπωση της τελικής έκφρασης
print(' '.join(result))