from typing import Optional, List, Tuple, NamedTuple

# from collections import Counter
import collections as c

Counter = c.Counter[str]


class NameCounts(NamedTuple):
    first: Optional[int]
    last: Optional[int]
    first_last: Optional[int]
    last_first_initial: Optional[int]


class Signature(NamedTuple):
    author_info_first: Optional[str]
    author_info_first_normalized_without_apostrophe: Optional[str]
    author_info_middle: Optional[str]
    author_info_middle_normalized_without_apostrophe: Optional[str]
    author_info_last_normalized: Optional[str]
    author_info_last: str
    author_info_suffix_normalized: Optional[str]
    author_info_suffix: Optional[str]
    author_info_first_normalized: Optional[str]
    author_info_middle_normalized: Optional[str]
    author_info_coauthors: Optional[List[str]]
    author_info_coauthor_blocks: Optional[List[str]]
    author_info_full_name: Optional[str]
    author_info_affiliations: List[str]
    author_info_affiliations_n_grams: Optional[Counter]
    author_info_coauthor_n_grams: Optional[Counter]
    author_info_email: Optional[str]
    author_info_email_prefix_ngrams: Optional[Counter]
    author_info_name_counts: Optional[NameCounts]
    author_info_position: int
    author_info_block: str
    author_info_given_block: Optional[str]
    author_info_estimated_gender: Optional[str]
    author_info_estimated_ethnicity: Optional[str]
    paper_id: int
    sourced_author_source: Optional[str]
    sourced_author_ids: List[str]
    author_id: Optional[int]
    signature_id: str


class Author(NamedTuple):
    author_name: str
    position: int


class Paper(NamedTuple):
    title: str
    has_abstract: Optional[bool]
    in_signatures: Optional[bool]
    is_english: Optional[bool]
    is_reliable: Optional[bool]
    predicted_language: Optional[str]
    title_ngrams_words: Optional[Counter]
    authors: List[Author]
    venue: Optional[str]
    journal_name: Optional[str]
    title_ngrams_chars: Optional[Counter]
    venue_ngrams: Optional[Counter]
    journal_ngrams: Optional[Counter]
    reference_details: Optional[Tuple[Counter, Counter, Counter, Counter]]
    year: Optional[int]
    references: Optional[List[int]]
    paper_id: int


class MiniPaper(NamedTuple):
    title: str
    venue: Optional[str]
    journal_name: Optional[str]
    authors: List[str]
