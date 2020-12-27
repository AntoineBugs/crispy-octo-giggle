from utils import str_norm


# Returns a copy of s where all instances
# of the character c have been deleted
def wipe_letter(s, c):
    new = ''.join(s.split(c))
    return new


# Wipes "outside" letters (the first and last ones)
def wipe_outer(s):
    beg = s[0]
    end = s[-1]
    new = wipe_letter(wipe_letter(s, beg), end)
    return new


# Wipes "inside" letters (the middle ones)
def wipe_inner(s):
    quot, rem = divmod(len(s), 2)
    nb = 2 - rem
    if nb == 1:
        mid = s[quot]
        new = wipe_letter(s, mid)
    else:
        mid1 = s[quot - 1]
        mid2 = s[quot]
        new = wipe_letter(wipe_letter(s, mid1), mid2)
    return new


# Iterated outer wipe, until another iteration
# would completely erase the string
def get_heart(name):
    old = str_norm(name)
    new = old
    while len(new) > 0:
        old = new
        new = wipe_outer(old)
    return old


# Iterated inner wipe, until another iteration
# would completely erase the string
def get_mantle(name):
    old = str_norm(name)
    new = old
    while len(new) > 0:
        old = new
        new = wipe_inner(old)
    return old


class GeneticProfile:

    def __init__(self, name):
        self.heart = get_heart(name)
        self.mantle = get_mantle(name)
        self.genes = self.heart + self.mantle

        self._compute_gene_adv()
        self._compute_ranks()

    # Computes the genetic advantages, based on
    # the vowels of the "genes"
    def _compute_gene_adv(self):
        ld = {letter: 1 for letter in 'aeiouy'}
        for x in ld:
            ld[x] += self.genes.count(x) * 25 / 100
        self.gene_adv = ld

    # Computes the purity and nobility indices,
    # by averaging the "heart" and "mantle" respectively
    def _compute_ranks(self):
        h = [ord(c) - ord('a') + 1 for c in self.heart]
        self.purity = sum(h) / len(h)

        m = [ord(c) - ord('a') + 1 for c in self.mantle]
        self.nobility = sum(m) / len(m)
