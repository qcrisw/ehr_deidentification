from typing import Optional
from dataclasses import dataclass, field

@dataclass
class DataTrainingArguments:
    """
    Arguments pertaining to what data we are going to input our model for training and eval.
    """
    task_name: Optional[str] = field(
        default="ner",
        metadata={"help": "The name of the task (ner, pos...)."}
    )
    notation: str = field(
        default="BIO",
        metadata={"help": "NER notation e.g BIO"},
    )
    ner_types: Optional[str] = field(
        default=None,
        metadata={"help": "Pass a list of NER types"},
    )
    train_file: Optional[str] = field(
        default=None,
        metadata={"help": "The input training data file (a csv or JSON file)."}
    )
    validation_file: Optional[str] = field(
        default=None,
        metadata={"help": "An optional input evaluation data file to evaluate on (a csv or JSON file)."},
    )
    test_file: Optional[str] = field(
        default=None,
        metadata={"help": "An optional input test data file to predict on (a csv or JSON file)."},
    )
    output_predictions_file: Optional[str] = field(
        default=None,
        metadata={"help": "A location where to write the output of the test data"},
    )
    text_column_name: Optional[str] = field(
        default='tokens',
        metadata={"help": "The column name of text to input in the file (a csv or JSON file)."}
    )
    label_column_name: Optional[str] = field(
        default='labels',
        metadata={"help": "The column name of label to input in the file (a csv or JSON file)."}
    )
    overwrite_cache: bool = field(
        default=False,
        metadata={"help": "Overwrite the cached training and evaluation sets"}
    )
    preprocessing_num_workers: Optional[int] = field(
        default=None,
        metadata={"help": "The number of processes to use for the preprocessing."},
    )
    pad_to_max_length: bool = field(
        default=False,
        metadata={
            "help": "Whether to pad all samples to model maximum sentence length. "
            "If False, will pad the samples dynamically when batching to the maximum length in the batch. More "
            "efficient on GPU but very bad for TPU."
        },
    )
    truncation: bool = field(
        default=True,
        metadata={
            "help": "Activates and controls truncation"
        },
    )
    max_length: int = field(
        default=512,
        metadata={
            "help": "Controls the maximum length to use by one of the truncation/padding parameters."
        },
    )
    do_lower_case: bool = field(
        default=False,
        metadata={
            "help": "Whether to lowercase the text"
        },
    )
    max_train_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of training examples to this "
            "value if set."
        },
    )
    max_eval_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of evaluation examples to this "
            "value if set."
        },
    )
    max_predict_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of prediction examples to this "
            "value if set."
        },
    )
    label_all_tokens: bool = field(
        default=False,
        metadata={
            "help": "Whether to put the label for one word on all tokens of generated by that word or just on the "
            "one (in which case the other tokens will have a padding index)."
        },
    )
    return_entity_level_metrics: bool = field(
        default=True,
        metadata={"help": "Whether to return all the entity levels during evaluation or just the overall ones."},
    )
    token_ignore_label: str = field(
        default='NA',
        metadata={"help": "The label that indicates where the tokens will be ignored in loss computation. Used for "
                          "indicating context tokens to the model"}
    )