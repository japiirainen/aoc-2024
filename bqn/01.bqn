#!/usr/bin/env bqn

⟨Num, Split, Count⟩ ← •Import "utils.bqn"

l‿r ← <˘⍉ Num¨ > ' 'Split¨ •FLines "../inputs/01.txt"

•Show +´ |-´ ∧¨l‿r

•Show +´ l× l Count r
