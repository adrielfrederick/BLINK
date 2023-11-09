import argparse
import blink.main_dense as main_dense
import blink.candidate_ranking.utils as utils

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--interactive", "-i", action="store_true", help="Interactive mode."
    )

    # test_data
    parser.add_argument(
        "--test_mentions", dest="test_mentions", type=str, help="Test Dataset."
    )
    parser.add_argument(
        "--test_entities", dest="test_entities", type=str, help="Test Entities."
    )

    # biencoder
    parser.add_argument(
        "--biencoder_model",
        dest="biencoder_model",
        type=str,
        default="models/biencoder_wiki_large.bin",
        help="Path to the biencoder model.",
    )
    parser.add_argument(
        "--biencoder_config",
        dest="biencoder_config",
        type=str,
        default="models/biencoder_wiki_large.json",
        help="Path to the biencoder configuration.",
    )
    parser.add_argument(
        "--entity_catalogue",
        dest="entity_catalogue",
        type=str,
        # default="models/tac_entity.jsonl",  # TAC-KBP
        default="models/entity.jsonl",  # ALL WIKIPEDIA!
        help="Path to the entity catalogue.",
    )
    parser.add_argument(
        "--entity_encoding",
        dest="entity_encoding",
        type=str,
        # default="models/tac_candidate_encode_large.t7",  # TAC-KBP
        default="models/all_entities_large.t7",  # ALL WIKIPEDIA!
        help="Path to the entity catalogue.",
    )

    # crossencoder
    parser.add_argument(
        "--crossencoder_model",
        dest="crossencoder_model",
        type=str,
        default="models/crossencoder_wiki_large.bin",
        help="Path to the crossencoder model.",
    )
    parser.add_argument(
        "--crossencoder_config",
        dest="crossencoder_config",
        type=str,
        default="models/crossencoder_wiki_large.json",
        help="Path to the crossencoder configuration.",
    )

    parser.add_argument(
        "--top_k",
        dest="top_k",
        type=int,
        default=10,
        help="Number of candidates retrieved by biencoder.",
    )

    # output folder
    parser.add_argument(
        "--output_path",
        dest="output_path",
        type=str,
        default="output",
        help="Path to the output.",
    )

    parser.add_argument(
        "--fast", dest="fast", action="store_true", help="only biencoder mode"
    )

    parser.add_argument(
        "--show_url",
        dest="show_url",
        action="store_true",
        help="whether to show entity url in interactive mode",
    )

    parser.add_argument(
        "--faiss_index", type=str, default=None, help="whether to use faiss index",
    )

    parser.add_argument(
        "--index_path", type=str, default=None, help="path to load indexer",
    )

    args = parser.parse_args()

    logger = utils.get_logger(args.output_path)

    models = main_dense.load_models(args, logger)
    main_dense.run(args, logger, *models)
