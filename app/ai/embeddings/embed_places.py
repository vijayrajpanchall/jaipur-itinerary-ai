"""
Embedding generation for places to enable semantic search.
"""
import pandas as pd
import numpy as np
from typing import List, Optional, Tuple
import os


class PlaceEmbeddings:
    def __init__(self, model_name: str = "text-embedding-ada-002"):
        self.model_name = model_name
        self.embeddings_cache = {}
        self.embeddings_file = "data/embeddings/place_embeddings.npy"
        self.metadata_file = "data/embeddings/place_metadata.csv"

    def generate_embeddings(self, places_df: pd.DataFrame) -> np.ndarray:
        """
        Generate embeddings for places data.

        Args:
            places_df: DataFrame containing places information

        Returns:
            NumPy array of embeddings
        """
        # Placeholder for embedding generation
        # In production, this would use OpenAI embeddings or similar
        embeddings = []

        for _, row in places_df.iterrows():
            # Create a text representation of the place
            text = self._create_place_text(row)

            # Generate embedding (placeholder - returns random vector)
            embedding = self._generate_embedding(text)
            embeddings.append(embedding)

        return np.array(embeddings)

    def _create_place_text(self, place_row: pd.Series) -> str:
        """Create a text representation of a place for embedding."""
        parts = []

        if "name" in place_row:
            parts.append(f"Name: {place_row['name']}")

        if "description" in place_row:
            parts.append(f"Description: {place_row['description']}")

        if "category" in place_row:
            parts.append(f"Category: {place_row['category']}")

        if "tags" in place_row:
            parts.append(f"Tags: {place_row['tags']}")

        return " | ".join(parts)

    def _generate_embedding(self, text: str) -> np.ndarray:
        """
        Generate embedding for text.
        This is a placeholder that returns a random vector.
        In production, use actual embedding model.
        """
        # Placeholder: return random 1536-dimensional vector (OpenAI embedding size)
        return np.random.randn(1536)

    def save_embeddings(self, embeddings: np.ndarray, places_df: pd.DataFrame):
        """Save embeddings and metadata to disk."""
        os.makedirs(os.path.dirname(self.embeddings_file), exist_ok=True)

        # Save embeddings
        np.save(self.embeddings_file, embeddings)

        # Save metadata
        places_df.to_csv(self.metadata_file, index=False)

    def load_embeddings(self) -> Tuple[Optional[np.ndarray], Optional[pd.DataFrame]]:
        """Load embeddings and metadata from disk."""
        if not os.path.exists(self.embeddings_file) or not os.path.exists(self.metadata_file):
            return None, None

        embeddings = np.load(self.embeddings_file)
        metadata = pd.read_csv(self.metadata_file)

        return embeddings, metadata

    def find_similar_places(
        self, query: str, places_df: pd.DataFrame, embeddings: np.ndarray, top_k: int = 5
    ) -> List[dict]:
        """
        Find places similar to the query using embeddings.

        Args:
            query: Search query
            places_df: DataFrame with places information
            embeddings: Pre-computed embeddings
            top_k: Number of results to return

        Returns:
            List of similar places with similarity scores
        """
        # Generate query embedding
        query_embedding = self._generate_embedding(query)

        # Calculate similarities (cosine similarity)
        similarities = self._cosine_similarity(query_embedding, embeddings)

        # Get top-k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        # Prepare results
        results = []
        for idx in top_indices:
            place = places_df.iloc[idx].to_dict()
            place["similarity_score"] = float(similarities[idx])
            results.append(place)

        return results

    def _cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> np.ndarray:
        """Calculate cosine similarity between vectors."""
        vec1_norm = vec1 / np.linalg.norm(vec1)
        vec2_norm = vec2 / np.linalg.norm(vec2, axis=1, keepdims=True)
        return np.dot(vec2_norm, vec1_norm)
