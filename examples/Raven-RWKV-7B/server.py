import logging

from model import RavenRWKVModel as Model
from simple_ai.api.grpc.chat.server import (
    LanguageModelServicer as ChatServicer,
    serve,
)

if __name__ == "__main__":
    import argparse

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", type=str, default="[::]:50051")
    args = parser.parse_args()

    logging.info(f"Starting gRPC server on {args.address}")
    model = Model()
    model_servicer = ChatServicer(model=Model())
    serve(address=args.address, model_servicer=model_servicer)