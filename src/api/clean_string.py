import re
import string


def remove_line_break(column): return re.sub(r"[\n]", "", column)
def convert_to_lowercase(column): return column.lower()


def remove_punctuations(column): return re.sub(
    f"[{re.escape(string.punctuation)}]", "", column)
def remove_words_inside_parentheses(
    column): return re.sub(r"[({\[].*[)}\]]", "", column)


def remove_numbers(column): return re.sub(r"\d", "", column)
def remove_other_signs(column): return re.sub(r"[%$][\w\.\,]*", "", column)
def remove_emails(column): return re.sub(r"\w+@\w+", "", column)
def remove_non_unicode_symbols(column): return re.sub(r"[“”’―]", "", column)
def remove_single_characters(column): return re.sub(
    r"\b[a-zA-Z]\b", "", column)


def remove_extra_whitespaces(column): return re.sub(r"  +", " ", column)
def remove_websites(column): return re.sub(r"^www\w+com$", "", column)


def remove_non_english_characters(
    column): return re.sub(r"[^a-zA-Z ]", "", column)


def remove_multi_repeat_characters(
    column): return re.sub(r"(\w)\1{2,}", "", column)


def remove_unusual_characters(column): return column.replace("\xa0", " ")


def clean_string(column):
    column = column.apply(remove_line_break)
    column = column.apply(convert_to_lowercase)
    column = column.apply(remove_punctuations)
    column = column.apply(remove_words_inside_parentheses)
    column = column.apply(remove_numbers)
    column = column.apply(remove_other_signs)
    column = column.apply(remove_emails)
    column = column.apply(remove_non_unicode_symbols)
    column = column.apply(remove_single_characters)
    column = column.apply(remove_unusual_characters)
    column = column.apply(remove_websites)
    column = column.apply(remove_non_english_characters)
    column = column.apply(remove_multi_repeat_characters)
    column = column.apply(remove_extra_whitespaces)
    return column
