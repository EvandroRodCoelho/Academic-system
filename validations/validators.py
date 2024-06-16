from pyswip import Prolog

prolog = Prolog()

prolog.assertz("especial(C) :- \+ char_type(C, alnum), C \= ' '")
prolog.assertz("contem_especial([C|_]) :- especial(C), !")
prolog.assertz("contem_especial([_|T]) :- contem_especial(T)")
prolog.assertz("numerico(C) :- char_type(C, digit)")
prolog.assertz("contem_numerico([C|_]) :- numerico(C), !")
prolog.assertz("contem_numerico([_|T]) :- contem_numerico(T)")
prolog.assertz("tamanho_max_campo(X) :- string_length(X, Length), Length =< 100")
prolog.assertz("tamanho_min_campo(X) :- string_length(X, Length), Length >= 3")
prolog.assertz("alfabetico(C) :- char_type(C, alpha)")
prolog.assertz("contem_alfabetico([C|_]) :- alfabetico(C), !")
prolog.assertz("contem_alfabetico([_|T]) :- contem_alfabetico(T)")


def string_to_list(s):
    return "[" + ",".join("'{}'".format(c) for c in s) + "]"


def validar_tamanho_campo(campo):
    tamanho_max = bool(list(prolog.query(f"tamanho_max_campo('{campo}')")))
    tamanho_min = bool(list(prolog.query(f"tamanho_min_campo('{campo}')")))

    if not tamanho_max or not tamanho_min:
        return False

    return True


def validar_caracteres_especiais(campo):
    contem_especial = bool(list(prolog.query(f"contem_especial({string_to_list(campo)})")))

    if contem_especial:
        return False

    return True


def validar_caracteres_numericos(campo):
    contem_numerico = bool(list(prolog.query("contem_numerico({})".format(string_to_list(campo)))))

    if contem_numerico:
        return False

    return True


def validar_caracteres_alfabeticos(campo):
    contem_alfabetico = bool(list(prolog.query(f"contem_alfabetico({string_to_list(campo)})")))

    if contem_alfabetico:
        return False

    return True
