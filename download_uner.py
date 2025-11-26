from socket import CAN_ERR_FLAG
import conllu

import datasets


_CITATION = r"""\
@misc{mayhew2023universal,
      title={Universal NER: A Gold-Standard Multilingual Named Entity Recognition Benchmark}, 
      author={Stephen Mayhew and Terra Blevins and Shuheng Liu and Marek Šuppa and Hila Gonen and Joseph Marvin Imperial and Börje F. Karlsson and Peiqin Lin and Nikola Ljubešić and LJ Miranda and Barbara Plank and Arij Riabi and Yuval Pinter},
      year={2023},
      eprint={2311.09122},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
"""  # noqa: W605

_DESCRIPTION = """\
Universal Named Entity Recognition (UNER) aims to fill a gap in multilingual NLP: high quality NER datasets in many languages with a shared tagset.

UNER is modeled after the Universal Dependencies project, in that it is intended to be a large community annotation effort with language-universal guidelines. Further, we use the same text corpora as Universal Dependencies.
"""

_NAMES = [
    "ceb_gja",
    "zh_gsd",
    "zh_gsdsimp",
    "zh_pud",
    "hr_set",
    "da_ddt",
    "en_ewt",
    "en_pud",
    "de_pud",
    "pt_bosque",
    "pt_pud",
    "ru_pud",
    "sr_set",
    "sk_snk",
    "sv_pud",
    "sv_talbanken",
    "tl_trg",
    "tl_ugnayan",
]

_DESCRIPTIONS = {
    "ceb_gja": "UD_Cebuano_GJA is a collection of annotated Cebuano sample sentences randomly taken from three different sources: community-contributed samples from the website Tatoeba, a Cebuano grammar book by Bunye & Yap (1971) and Tanangkinsing's reference grammar on Cebuano (2011). This project is currently work in progress.",
    "zh_gsd": "Traditional Chinese Universal Dependencies Treebank annotated and converted by Google.",
    "zh_gsdsimp": "Simplified Chinese Universal Dependencies dataset converted from the GSD (traditional) dataset with manual corrections.",
    "zh_pud": "This is a part of the Parallel Universal Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on Multilingual Parsing from Raw Text to Universal Dependencies.",
    "hr_set": "The Croatian UD treebank is based on the extension of the SETimes-HR corpus, the hr500k corpus.",
    "da_ddt": "The Danish UD treebank is a conversion of the Danish Dependency Treebank.",
    "en_ewt": "A Gold Standard Universal Dependencies Corpus for English, built over the source material of the English Web Treebank LDC2012T13 (https://catalog.ldc.upenn.edu/LDC2012T13).",
    "en_pud": "This is the English portion of the Parallel Universal Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on Multilingual Parsing from Raw Text to Universal Dependencies (http://universaldependencies.org/conll17/).",
    "de_pud": "This is a part of the Parallel Universal Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on Multilingual Parsing from Raw Text to Universal Dependencies.",
    "pt_bosque": "This Universal Dependencies (UD) Portuguese treebank is based on the Constraint Grammar converted version of the Bosque, which is part of the Floresta Sintá(c)tica treebank. It contains both European (CETEMPúblico) and Brazilian (CETENFolha) variants.",
    "pt_pud": "This is a part of the Parallel Universal Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on Multilingual Parsing from Raw Text to Universal Dependencies.",
    "ru_pud": "This is a part of the Parallel Universal Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on Multilingual Parsing from Raw Text to Universal Dependencies.",
    "sr_set": "The Serbian UD treebank is based on the [SETimes-SR](http://hdl.handle.net/11356/1200) corpus and additional news documents from the Serbian web.",
    "sk_snk": "The Slovak UD treebank is based on data originally annotated as part of the Slovak National Corpus, following the annotation style of the Prague Dependency Treebank.",
    "sv_pud": "Swedish-PUD is the Swedish part of the Parallel Universal Dependencies (PUD) treebanks.",
    "sv_talbanken": "The Swedish-Talbanken treebank is based on Talbanken, a treebank developed at Lund University in the 1970s.",
    "tl_trg": "UD_Tagalog-TRG is a UD treebank manually annotated using sentences from a grammar book.",
    "tl_ugnayan": "Ugnayan is a manually annotated Tagalog treebank currently composed of educational fiction and nonfiction text. The treebank is under development at the University of the Philippines.",
}

_PREFIX = "https://raw.githubusercontent.com/UniversalNER/"

_UNER_DATASETS = {
    "ceb_gja": {
        "test": "UNER_Cebuano-GJA/master/ceb_gja-ud-test.iob2",
    },
    "zh_gsd": {
        "train": "UNER_Chinese-GSD/master/zh_gsd-ud-train.iob2",
        "dev": "UNER_Chinese-GSD/master/zh_gsd-ud-dev.iob2",
        "test": "UNER_Chinese-GSD/master/zh_gsd-ud-test.iob2",
    },
    "zh_gsdsimp": {
        "train": "UNER_Chinese-GSDSIMP/master/zh_gsdsimp-ud-train.iob2",
        "dev": "UNER_Chinese-GSDSIMP/master/zh_gsdsimp-ud-dev.iob2",
        "test": "UNER_Chinese-GSDSIMP/master/zh_gsdsimp-ud-test.iob2",
    },
    "zh_pud": {
        "test": "UNER_Chinese-PUD/master/zh_pud-ud-test.iob2",
    },
    "hr_set": {
        "train": "UNER_Croatian-SET/main/hr_set-ud-train.iob2",
        "dev": "UNER_Croatian-SET/main/hr_set-ud-dev.iob2",
        "test": "UNER_Croatian-SET/main/hr_set-ud-test.iob2",
    },
    "da_ddt": {
        "train": "UNER_Danish-DDT/main/da_ddt-ud-train.iob2",
        "dev": "UNER_Danish-DDT/main/da_ddt-ud-dev.iob2",
        "test": "UNER_Danish-DDT/main/da_ddt-ud-test.iob2",
    },
    "en_ewt": {
        "train": "UNER_English-EWT/master/en_ewt-ud-train.iob2",
        "dev": "UNER_English-EWT/master/en_ewt-ud-dev.iob2",
        "test": "UNER_English-EWT/master/en_ewt-ud-test.iob2",
    },
    "en_pud": {
        "test": "UNER_English-PUD/master/en_pud-ud-test.iob2",
    },
    "de_pud": {
        "test": "UNER_German-PUD/master/de_pud-ud-test.iob2",
    },
    "pt_bosque": {
        "train": "UNER_Portuguese-Bosque/master/pt_bosque-ud-train.iob2",
        "dev": "UNER_Portuguese-Bosque/master/pt_bosque-ud-dev.iob2",
        "test": "UNER_Portuguese-Bosque/master/pt_bosque-ud-test.iob2",
    },
    "pt_pud": {
        "test": "UNER_Portuguese-PUD/master/pt_pud-ud-test.iob2",
    },
    "ru_pud": {
        "test": "UNER_Russian-PUD/master/ru_pud-ud-test.iob2",
    },
    "sr_set": {
        "train": "UNER_Serbian-SET/main/sr_set-ud-train.iob2",
        "dev": "UNER_Serbian-SET/main/sr_set-ud-dev.iob2",
        "test": "UNER_Serbian-SET/main/sr_set-ud-test.iob2",
    },
    "sk_snk": {
        "train": "UNER_Slovak-SNK/master/sk_snk-ud-train.iob2",
        "dev": "UNER_Slovak-SNK/master/sk_snk-ud-dev.iob2",
        "test": "UNER_Slovak-SNK/master/sk_snk-ud-test.iob2",
    },
    "sv_pud": {
        "test": "UNER_Swedish-PUD/master/sv_pud-ud-test.iob2",
    },
    "sv_talbanken": {
        "train": "UNER_Swedish-Talbanken/master/sv_talbanken-ud-train.iob2",
        "dev": "UNER_Swedish-Talbanken/master/sv_talbanken-ud-dev.iob2",
        "test": "UNER_Swedish-Talbanken/master/sv_talbanken-ud-test.iob2",
    },
    "tl_trg": {
        "test": "UNER_Tagalog-TRG/master/tl_trg-ud-test.iob2",
    },
    "tl_ugnayan": {
        "test": "UNER_Tagalog-Ugnayan/master/tl_ugnayan-ud-test.iob2",
    },
}


class UniversalNerConfig(datasets.BuilderConfig):
    """BuilderConfig for Universal NER"""

    def __init__(self, data_url, **kwargs):
        super(UniversalNerConfig, self).__init__(version=datasets.Version("1.0.0", ""), **kwargs)

        self.data_url = data_url


class UniversalNer(datasets.GeneratorBasedBuilder):
    VERSION = datasets.Version("1.0.0")
    BUILDER_CONFIGS = [
        UniversalNerConfig(
            name=name,
            description=_DESCRIPTIONS[name],
            data_url="https://github.com/UniversalNER/" + _UNER_DATASETS[name]["test"].split("/")[0],
        )
        for name in _NAMES
    ]
    BUILDER_CONFIG_CLASS = UniversalNerConfig

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "idx": datasets.Value("string"),
                    "text": datasets.Value("string"),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    "ner_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "O",
                                "B-PER",
                                "I-PER",
                                "B-ORG",
                                "I-ORG",
                                "B-LOC",
                                "I-LOC",
                            ]
                        )
                    ),
                    "annotator": datasets.Sequence(datasets.Value("string")),
                }
            ),
            supervised_keys=None,
            homepage="https://www.universalner.org/",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns generator for dataset splits."""
        urls_to_download = {}
        for split, address in _UNER_DATASETS[self.config.name].items():
            urls_to_download[split] = []
            if isinstance(address, list):
                for add in address:
                    urls_to_download[split].append(_PREFIX + add)
            else:
                urls_to_download[split].append(_PREFIX + address)

        downloaded_files = dl_manager.download_and_extract(urls_to_download)
        splits = []

        if "train" in downloaded_files:
            splits.append(
                datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train"]})
            )

        if "dev" in downloaded_files:
            splits.append(
                datasets.SplitGenerator(
                    name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["dev"]}
                )
            )

        if "test" in downloaded_files:
            splits.append(
                datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": downloaded_files["test"]})
            )

        return splits

    def _generate_examples(self, filepath):
        id = 0
        column_names = ('id', 'token', 'tag', 'misc', 'annotator')
        for path in filepath:
            with open(path, "r", encoding="utf-8") as data_file:
                sentences = list(conllu.parse_incr(data_file, fields=column_names))
                for sent in sentences:
                    if "sent_id" in sent.metadata:
                        idx = sent.metadata["sent_id"]
                    else:
                        idx = id

                    tokens = [token["token"] for token in sent]
                    actual_tags = [token["tag"] for token in sent]

                    # Workaround for OTH and B-O
                    # See: https://github.com/UniversalNER/uner_code/blob/master/prepare_data.py#L22
                    fixed_tags = []

                    for actual_tag in actual_tags:
                        if "OTH" in actual_tag or actual_tag == "B-O":
                            actual_tag = "O"
                        fixed_tags.append(actual_tag)

                    annotator = [token["annotator"] for token in sent]

                    if "text" in sent.metadata:
                        txt = sent.metadata["text"]
                    else:
                        txt = " ".join(tokens)

                    yield id, {
                        "idx": str(idx),
                        "text": txt,
                        "tokens": tokens,
                        "ner_tags": fixed_tags,
                        "annotator": annotator,
                    }
                    id += 1


if __name__ == "__main__":
    for lang in _NAMES:
        builder = UniversalNer(config_name=lang)
        builder.download_and_prepare()
        dataset = builder.as_dataset()
        dataset = dataset.push_to_hub("BramVanroy/universalner", config_name=lang)