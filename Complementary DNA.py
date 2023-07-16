#問題
# https://www.codewars.com/kata/554e4a2f232cdd87d9000038

dna_dict = {'G':'C','C':'G','A':'T','T':'A'}
def DNA_strand(dna):
    return ''.join(list(map(lambda m:dna_dict[m],dna)))