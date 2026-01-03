"""
Enhanced visualization components for The Falcon Press Office
Advanced 3D visualizations, interactive plots, and analysis tools
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

class AdvancedVisualizer:
    """Advanced visualization suite for Relational Sphere analysis"""
    
    def __init__(self):
        self.color_schemes = {
            'viridis': 'viridis',
            'plasma': 'plasma', 
            'inferno': 'inferno',
            'magma': 'magma',
            'cividis': 'cividis'
        }
    
    def create_interactive_sphere(self, coordinates, quantum_signatures, scale=1.0):
        """Create interactive 3D sphere visualization with Plotly"""
        # Convert coordinates to arrays
        points = np.array(list(coordinates.values()))
        
        # Apply scaling
        points = points * scale
        
        # Extract coordinates
        x, y, z = points[:, 0], points[:, 1], points[:, 2]
        
        # Create colors based on quantum signatures
        colors = [hash(sig) % 100 for sig in quantum_signatures.values()]
        
        # Create 3D scatter plot
        fig = go.Figure(data=[go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=5,
                color=colors,
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Quantum Signature"),
                opacity=0.8
            ),
            text=list(quantum_signatures.keys()),
            hovertemplate='<b>%{text}</b><br>' +
                         'X: %{x:.2f}<br>' +
                         'Y: %{y:.2f}<br>' +
                         'Z: %{z:.2f}<extra></extra>'
        )])
        
        # Update layout
        fig.update_layout(
            title='Interactive Relational Sphere Visualization',
            scene=dict(
                xaxis_title='X Coordinate',
                yaxis_title='Y Coordinate', 
                zaxis_title='Z Coordinate',
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.5)
                )
            ),
            width=900,
            height=700
        )
        
        return fig
    
    def create_collision_network(self, collisions, coordinates):
        """Create network visualization of data collisions"""
        G = nx.Graph()
        
        # Add nodes
        for coord_id in coordinates.keys():
            G.add_node(coord_id)
        
        # Add collision edges
        for id1, id2, distance in collisions:
            G.add_edge(id1, id2, weight=distance)
        
        # Create layout
        pos = nx.spring_layout(G, k=1, iterations=50)
        
        # Extract edge coordinates for Plotly
        edge_x = []
        edge_y = []
        edge_info = []
        
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
            edge_info.append(f"{edge[0]} - {edge[1]}")
        
        # Create edge trace
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )
        
        # Create node trace
        node_x = []
        node_y = []
        node_text = []
        node_colors = []
        
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(node)
            # Color based on collision count
            node_colors.append(G.degree(node))
        
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            text=node_text,
            marker=dict(
                showscale=True,
                colorscale='YlOrRd',
                size=10,
                color=node_colors,
                colorbar=dict(title="Collision Count"),
                line=dict(width=2)
            )
        )
        
        # Create figure
        fig = go.Figure(data=[edge_trace, node_trace],
                       layout=go.Layout(
                           title='Data Collision Network',
                           titlefont_size=16,
                           showlegend=False,
                           hovermode='closest',
                           margin=dict(b=20,l=5,r=5,t=40),
                           annotations=[ dict(
                               text="Collision connections between data points",
                               showarrow=False,
                               xref="paper", yref="paper",
                               x=0.005, y=-0.002,
                               xanchor='left', yanchor='bottom',
                               font=dict(color="#888", size=12)
                           )],
                           xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                           yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                        )
        
        return fig
    
    def create_sentiment_heatmap(self, sentiment_data):
        """Create sentiment analysis heatmap"""
        # Prepare data
        topics = list(sentiment_data.keys())
        sources = [f"Source_{i}" for i in range(len(list(sentiment_data.values())[0]) if sentiment_data.values() else 10)]
        
        # Create matrix (simulated for demo)
        matrix = np.random.random((len(topics), len(sources)))
        
        # Create heatmap
        fig = go.Figure(data=go.Heatmap(
            z=matrix,
            x=sources,
            y=topics,
            colorscale='RdBu',
            zmid=0,
            hoverongaps=False,
            hovertemplate='Topic: %{y}<br>Source: %{x}<br>Sentiment: %{z:.3f}<extra></extra>'
        ))
        
        fig.update_layout(
            title='Global Sentiment Analysis Heatmap',
            xaxis_title='News Sources',
            yaxis_title='Topics',
            width=900,
            height=600
        )
        
        return fig
    
    def create_language_trends_plot(self, language_data):
        """Create language usage trends visualization"""
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Language Distribution', 'Usage Over Time', 
                          'Regional Distribution', 'Sentiment by Language'),
            specs=[[{"type": "pie"}, {"type": "scatter"}],
                   [{"type": "bar"}, {"type": "box"}]]
        )
        
        # Language distribution pie chart
        languages = list(language_data.get('dominant_languages', {}).keys())
        counts = list(language_data.get('dominant_languages', {}).values())
        
        fig.add_trace(
            go.Pie(labels=languages, values=counts, name="Distribution"),
            row=1, col=1
        )
        
        # Usage over time (simulated)
        time_periods = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        for i, lang in enumerate(languages[:3]):
            trends = np.random.random(6) * 100
            fig.add_trace(
                go.Scatter(x=time_periods, y=trends, mode='lines+markers', name=lang),
                row=1, col=2
            )
        
        # Regional distribution
        regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']
        fig.add_trace(
            go.Bar(x=regions, y=np.random.random(5) * 50, name="Regional"),
            row=2, col=1
        )
        
        # Sentiment by language
        for i, lang in enumerate(languages[:3]):
            sentiments = np.random.normal(0, 0.3, 30)
            fig.add_trace(
                go.Box(y=sentiments, name=lang),
                row=2, col=2
            )
        
        fig.update_layout(
            title='Language Trends Analysis',
            height=800,
            showlegend=False
        )
        
        return fig
    
    def create_manipulation_factors_radar(self, factors_data):
        """Create radar chart for manipulation factors"""
        categories = ['Bias Score', 'Source Credibility', 'Fact Accuracy', 
                     'Emotional Language', 'Clickbait Level', 'Verification Status']
        
        # Create radar chart
        fig = go.Figure()
        
        # Add multiple sources for comparison
        sources = ['Mainstream', 'Alternative', 'Social Media', 'State Media']
        colors = ['blue', 'red', 'green', 'orange']
        
        for i, source in enumerate(sources):
            values = np.random.random(6)  # Simulated values
            values = np.concatenate([values, [values[0]]])  # Close the radar
            
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories + [categories[0]],
                fill='toself',
                name=source,
                line_color=colors[i]
            ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )),
            title="Manipulation Factors Analysis",
            height=600
        )
        
        return fig
    
    def create_geometric_distribution_plot(self, coordinates, properties):
        """Create geometric distribution analysis"""
        # Extract coordinates
        points = np.array(list(coordinates.values()))
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('3D Distribution', 'XY Projection', 
                          'Density Heatmap', 'Cluster Analysis'),
            specs=[[{"type": "scatter3d"}, {"type": "scatter"}],
                   [{"type": "histogram2d"}, {"type": "scatter"}]]
        )
        
        # 3D distribution
        fig.add_trace(
            go.Scatter3d(
                x=points[:, 0], y=points[:, 1], z=points[:, 2],
                mode='markers',
                marker=dict(size=3, color=points[:, 2], colorscale='Viridis'),
                showlegend=False
            ),
            row=1, col=1
        )
        
        # XY projection
        fig.add_trace(
            go.Scatter(
                x=points[:, 0], y=points[:, 1],
                mode='markers',
                marker=dict(size=5, opacity=0.6),
                showlegend=False
            ),
            row=1, col=2
        )
        
        # Density heatmap
        fig.add_trace(
            go.Histogram2d(
                x=points[:, 0], y=points[:, 1],
                colorscale='Viridis',
                showlegend=False
            ),
            row=2, col=1
        )
        
        # Cluster analysis (K-means)
        kmeans = KMeans(n_clusters=5, random_state=42)
        clusters = kmeans.fit_predict(points)
        
        fig.add_trace(
            go.Scatter(
                x=points[:, 0], y=points[:, 1],
                mode='markers',
                marker=dict(color=clusters, colorscale='Rainbow', size=5),
                showlegend=False
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            title='Geometric Distribution Analysis',
            height=800
        )
        
        return fig
    
    def create_consensus_timeline(self, consensus_data):
        """Create consensus evolution timeline"""
        fig = go.Figure()
        
        topics = list(consensus_data.keys())
        dates = pd.date_range('2024-01-01', periods=30, freq='D')
        
        for topic in topics:
            # Simulate consensus evolution
            values = np.random.random(30) * 0.8 + 0.2
            values = np.convolve(values, np.ones(3)/3, mode='same')  # Smooth
            
            fig.add_trace(go.Scatter(
                x=dates, y=values,
                mode='lines+markers',
                name=topic,
                line=dict(width=2)
            ))
        
        fig.update_layout(
            title='Global Consensus Evolution Over Time',
            xaxis_title='Date',
            yaxis_title='Consensus Score',
            height=500,
            hovermode='x unified'
        )
        
        return fig
    
    def create_problematic_affairs_sunburst(self, problematic_data):
        """Create sunburst chart for problematic affairs"""
        labels = []
        parents = []
        values = []
        
        # Create hierarchical data
        main_categories = ['Conflicts', 'Crises', 'Disputes', 'Concerns']
        
        for category in main_categories:
            labels.append(category)
            parents.append('')
            values.append(np.random.randint(5, 20))
            
            # Add subcategories
            subcategories = [f'{category}_{i}' for i in range(3)]
            for subcat in subcategories:
                labels.append(subcat)
                parents.append(category)
                values.append(np.random.randint(1, 10))
        
        fig = go.Figure(go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            branchvalues="total",
            hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percentParent:.1%}<extra></extra>'
        ))
        
        fig.update_layout(
            title="Problematic Affairs Distribution",
            margin=dict(t=0, l=0, r=0, b=0)
        )
        
        return fig
    
    def create_government_perceptions_gauge(self, perception_data):
        """Create gauge chart for government perceptions"""
        fig = make_subplots(
            rows=2, cols=3,
            specs=[[{"type": "indicator"}]*3]*2,
            subplot_titles=['Trust Level', 'Approval Rating', 'Policy Sentiment',
                          'Economic Confidence', 'Security Perception', 'International Standing']
        )
        
        metrics = ['Trust Level', 'Approval Rating', 'Policy Sentiment',
                  'Economic Confidence', 'Security Perception', 'International Standing']
        values = np.random.random(6) * 100
        
        for i, (metric, value) in enumerate(zip(metrics, values)):
            fig.add_trace(
                go.Indicator(
                    mode="gauge+number+delta",
                    value=value,
                    domain={'row': i//3, 'column': i%3},
                    title={'text': metric},
                    delta={'reference': 50},
                    gauge={
                        'axis': {'range': [None, 100]},
                        'bar': {'color': "darkblue"},
                        'steps': [
                            {'range': [0, 33], 'color': "lightgray"},
                            {'range': [33, 66], 'color': "gray"},
                            {'range': [66, 100], 'color': "lightblue"}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 80
                        }
                    }
                ),
                row=i//3+1, col=i%3+1
            )
        
        fig.update_layout(
            title="Government Perceptions Dashboard",
            height=600
        )
        
        return fig
    
    def export_visualization(self, fig, filename, format='html'):
        """Export visualization to file"""
        if format == 'html':
            fig.write_html(filename)
        elif format == 'png':
            fig.write_image(filename)
        elif format == 'pdf':
            fig.write_image(filename)
        elif format == 'svg':
            fig.write_image(filename)

class DataProcessor:
    """Enhanced data processing algorithms"""
    
    def __init__(self):
        self.processing_algorithms = {
            'sentiment_analysis': self.analyze_sentiment,
            'topic_modeling': self.extract_topics,
            'entity_recognition': self.extract_entities,
            'keyword_extraction': self.extract_keywords,
            'language_detection': self.detect_language,
            'readability_analysis': self.analyze_readability
        }
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of text"""
        # Simple sentiment analysis (would use NLP library in production)
        positive_words = ['good', 'great', 'excellent', 'positive', 'success', 'progress']
        negative_words = ['bad', 'terrible', 'negative', 'failure', 'crisis', 'problem']
        
        words = text.lower().split()
        pos_count = sum(1 for word in words if word in positive_words)
        neg_count = sum(1 for word in words if word in negative_words)
        
        total_sentiment_words = pos_count + neg_count
        if total_sentiment_words == 0:
            return 0.0
        
        return (pos_count - neg_count) / total_sentiment_words
    
    def extract_topics(self, text, num_topics=5):
        """Extract main topics from text"""
        # Simple topic extraction (would use advanced NLP in production)
        topic_keywords = {
            'Politics': ['government', 'policy', 'election', 'political', 'democracy'],
            'Economy': ['economy', 'economic', 'market', 'finance', 'business'],
            'Health': ['health', 'medical', 'disease', 'healthcare', 'medicine'],
            'Environment': ['environment', 'climate', 'pollution', 'sustainability', 'green'],
            'Technology': ['technology', 'digital', 'innovation', 'software', 'internet']
        }
        
        words = text.lower().split()
        topic_scores = {}
        
        for topic, keywords in topic_keywords.items():
            score = sum(1 for word in words if word in keywords)
            topic_scores[topic] = score
        
        # Return top topics
        sorted_topics = sorted(topic_scores.items(), key=lambda x: x[1], reverse=True)
        return [topic for topic, score in sorted_topics[:num_topics] if score > 0]
    
    def extract_entities(self, text):
        """Extract named entities from text"""
        # Simple entity extraction (would use NER library in production)
        import re
        
        # Extract potential entities (capitalized words/phrases)
        entities = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', text)
        return list(set(entities))
    
    def extract_keywords(self, text, num_keywords=10):
        """Extract keywords from text"""
        # Simple keyword extraction based on frequency
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
        word_freq = {}
        
        for word in words:
            if word not in ['that', 'this', 'with', 'from', 'they', 'have', 'been']:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in sorted_words[:num_keywords]]
    
    def detect_language(self, text):
        """Detect language of text"""
        # Simple language detection (would use specialized library in production)
        language_indicators = {
            'en': ['the', 'and', 'is', 'in', 'to', 'of', 'a', 'that', 'it', 'with'],
            'es': ['el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'es', 'se'],
            'fr': ['le', 'de', 'et', 'à', 'un', 'il', 'être', 'et', 'en', 'avoir'],
            'de': ['der', 'die', 'und', 'in', 'den', 'von', 'zu', 'das', 'mit', 'sich'],
            'zh': ['的', '了', '在', '是', '我', '有', '和', '就', '不', '人'],
            'ar': ['في', 'من', 'إلى', 'على', 'أن', 'هذا', 'التي', 'كان', 'كما', 'له']
        }
        
        text_lower = text.lower()
        scores = {}
        
        for lang, indicators in language_indicators.items():
            score = sum(1 for indicator in indicators if indicator in text_lower)
            scores[lang] = score
        
        if scores:
            detected_lang = max(scores, key=scores.get)
            return detected_lang if scores[detected_lang] > 0 else 'unknown'
        
        return 'unknown'
    
    def analyze_readability(self, text):
        """Analyze readability of text"""
        sentences = text.split('.')
        words = text.split()
        
        if not sentences or not words:
            return 0.0
        
        avg_sentence_length = len(words) / len(sentences)
        avg_word_length = sum(len(word) for word in words) / len(words)
        
        # Simple readability score
        readability = 100 - (avg_sentence_length * 1.5) - (avg_word_length * 2)
        return max(0, min(100, readability))
    
    def process_document(self, text, algorithms=None):
        """Process document with specified algorithms"""
        if algorithms is None:
            algorithms = list(self.processing_algorithms.keys())
        
        results = {}
        
        for algorithm in algorithms:
            if algorithm in self.processing_algorithms:
                try:
                    results[algorithm] = self.processing_algorithms[algorithm](text)
                except Exception as e:
                    results[algorithm] = f"Error: {str(e)}"
        
        return results

# Utility functions for visualization integration
def create_dashboard_visualizations(sphere, analysis_data):
    """Create comprehensive dashboard visualizations"""
    visualizer = AdvancedVisualizer()
    
    visualizations = {}
    
    # Sphere visualization
    if sphere and sphere.coordinates:
        visualizations['sphere'] = visualizer.create_interactive_sphere(
            sphere.coordinates, sphere.quantum_signatures
        )
    
    # Collision network
    if sphere and sphere.geometric_collisions:
        visualizations['collisions'] = visualizer.create_collision_network(
            sphere.geometric_collisions, sphere.coordinates
        )
    
    # Sentiment heatmap
    if 'sentiment' in analysis_data:
        visualizations['sentiment'] = visualizer.create_sentiment_heatmap(
            analysis_data['sentiment']
        )
    
    # Language trends
    if 'language' in analysis_data:
        visualizations['language'] = visualizer.create_language_trends_plot(
            analysis_data['language']
        )
    
    # Manipulation factors
    if 'manipulation' in analysis_data:
        visualizations['manipulation'] = visualizer.create_manipulation_factors_radar(
            analysis_data['manipulation']
        )
    
    return visualizations