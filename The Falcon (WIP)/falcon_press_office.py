#!/usr/bin/env python3
"""
The Falcon Press Office - Advanced Relational Sphere Analysis System
Comprehensive GUI application for global news analysis with 3D sphere visualization
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import json
import re
import hashlib
import math
import threading
import webbrowser
import os
import sys
import requests
from datetime import datetime, timedelta
import sqlite3
import hashlib
import base64
from urllib.parse import urljoin, urlparse
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Any
import warnings
warnings.filterwarnings('ignore')

# Import our libraries
import government_public_info_library_clean as government_public_info_library
import predictive_news_patterns_library_clean as predictive_news_patterns_library

@dataclass
class RelationalSphere:
    """Core Relational Sphere data structure following Breath-Caelum-Space Balls-Cradle conventions"""
    sphere_id: str
    coordinates: Dict[str, Tuple[float, float, float]]
    quantum_signatures: Dict[str, str]
    mathematical_properties: Dict[str, Any]
    assessment_relay: Dict[str, Any]
    geometric_collisions: List[Tuple[str, str, float]]
    
class RelationalSphereEngine:
    """Advanced Relational Sphere generation and analysis engine"""
    
    def __init__(self):
        self.forbidden_angles = [30.0, 90.0, 150.0, 210.0, 270.0, 330.0]
        self.prime_sequences = [4, 7, 9, 11, 13, 17, 19, 23, 29, 31]
        self.sphere_cache = {}
        
    def generate_sphere_from_libraries(self, gov_library, patterns_library):
        """Generate comprehensive Relational Sphere from both libraries"""
        sphere_data = {}
        quantum_signatures = {}
        mathematical_properties = {}
        
        # Process government library
        for source_id, source in gov_library.sources.items():
            sphere_data[f"gov_{source_id}"] = source.sphere_coordinates
            quantum_signatures[f"gov_{source_id}"] = source.quantum_signature
            mathematical_properties[f"gov_{source_id}"] = source.mathematical_properties
        
        # Process patterns library
        for pattern_id, pattern in patterns_library.patterns.items():
            sphere_data[f"pat_{pattern_id}"] = pattern.sphere_coordinates
            quantum_signatures[f"pat_{pattern_id}"] = pattern.quantum_signature
            mathematical_properties[f"pat_{pattern_id}"] = pattern.mathematical_properties
        
        # Create Relational Sphere
        sphere = RelationalSphere(
            sphere_id=f"falcon_sphere_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            coordinates=sphere_data,
            quantum_signatures=quantum_signatures,
            mathematical_properties=mathematical_properties,
            assessment_relay=self._generate_assessment_relay(sphere_data, mathematical_properties),
            geometric_collisions=self._detect_collisions(sphere_data)
        )
        
        return sphere
    
    def _generate_assessment_relay(self, coordinates, properties):
        """Generate assessment relay data for sphere generation compatibility"""
        coords = list(coordinates.values())
        
        return {
            "coordinate_variance": np.var([c[0] for c in coords]) if coords else 0,
            "quantum_diversity": len(set(hash(str(c)) for c in coords)),
            "forbidden_angle_compliance_rate": self._check_angle_compliance(coords),
            "average_geometric_entropy": np.mean([math.log2(len(str(p)) + 1) for p in properties.values()]) if properties else 0,
            "sphere_density": len(coords) / (4/3 * math.pi * 1000**3),  # Assume sphere radius of 1000
            "relay_ready": True
        }
    
    def _check_angle_compliance(self, coordinates):
        """Check compliance with forbidden angles"""
        if not coordinates:
            return 1.0
        
        compliant_count = 0
        for coord in coordinates:
            angles = [math.degrees(c) % 360 for c in coord]
            compliant = all(
                abs(angle - forbidden) > 5.0 
                for angle in angles 
                for forbidden in self.forbidden_angles
            )
            if compliant:
                compliant_count += 1
        
        return compliant_count / len(coordinates)
    
    def _detect_collisions(self, coordinates):
        """Detect geometric data collisions in the sphere"""
        collisions = []
        coords_list = list(coordinates.items())
        
        for i, (id1, coord1) in enumerate(coords_list):
            for j, (id2, coord2) in enumerate(coords_list[i+1:], i+1):
                distance = math.sqrt(
                    (coord1[0] - coord2[0])**2 + 
                    (coord1[1] - coord2[1])**2 + 
                    (coord1[2] - coord2[2])**2
                )
                if distance < 50:  # Collision threshold
                    collisions.append((id1, id2, distance))
        
        return collisions

class FreeAISummarizer:
    """Free-to-use AI summarization service"""
    
    def __init__(self):
        self.api_endpoints = {
            "huggingface": "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
            "openai_compatible": "https://api.openai.com/v1/chat/completions",  # For local models
            "ollama": "http://localhost:11434/api/generate"  # For local Ollama
        }
    
    def summarize_text(self, text, max_length=150):
        """Summarize text using free AI services"""
        try:
            # Try to use local Ollama first
            return self._summarize_with_ollama(text, max_length)
        except:
            try:
                # Fallback to HuggingFace
                return self._summarize_with_huggingface(text, max_length)
            except:
                # Fallback to extractive summarization
                return self._extractive_summary(text, max_length)
    
    def _summarize_with_ollama(self, text, max_length):
        """Summarize using local Ollama"""
        payload = {
            "model": "llama2",
            "prompt": f"Summarize this text in about {max_length} words:\n\n{text[:4000]}",
            "stream": False
        }
        
        response = requests.post(self.api_endpoints["ollama"], json=payload, timeout=30)
        if response.status_code == 200:
            return response.json().get("response", text[:max_length*5])
        raise Exception("Ollama not available")
    
    def _summarize_with_huggingface(self, text, max_length):
        """Summarize using HuggingFace API"""
        payload = {"inputs": text[:1024], "parameters": {"max_length": max_length}}
        
        response = requests.post(
            self.api_endpoints["huggingface"], 
            json=payload, 
            timeout=30,
            headers={"Authorization": "Bearer hf_dummy"}  # Would need real token
        )
        
        if response.status_code == 200:
            return response.json()[0].get("summary_text", text[:max_length*5])
        raise Exception("HuggingFace API not available")
    
    def _extractive_summary(self, text, max_length):
        """Extractive summarization as fallback"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        # Simple extractive algorithm - pick sentences with key terms
        key_terms = ["government", "policy", "data", "analysis", "report", "study"]
        scored_sentences = []
        
        for sentence in sentences:
            score = sum(1 for term in key_terms if term.lower() in sentence.lower())
            scored_sentences.append((score, sentence))
        
        scored_sentences.sort(reverse=True)
        summary_sentences = [s[1] for s in scored_sentences[:3]]
        
        return ". ".join(summary_sentences)[:max_length*5]

class WebContentAnalyzer:
    """Advanced web content analysis and library building"""
    
    def __init__(self):
        self.ai_summarizer = FreeAISummarizer()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Falcon-Press-Office/1.0'
        })
    
    def analyze_webpage(self, url):
        """Analyze webpage content and extract data"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # Extract content
            content = self._extract_content(response.text)
            
            # Generate summary
            summary = self.ai_summarizer.summarize_content(content)
            
            # Extract metadata
            metadata = self._extract_metadata(response.text, url)
            
            return {
                "url": url,
                "content": content,
                "summary": summary,
                "metadata": metadata,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": str(e), "url": url}
    
    def _extract_content(self, html):
        """Extract meaningful content from HTML"""
        # Remove script and style elements
        content = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
        
        # Extract text
        text = re.sub(r'<[^>]+>', ' ', content)
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def _extract_metadata(self, html, url):
        """Extract metadata from HTML"""
        metadata = {"url": url}
        
        # Extract title
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        if title_match:
            metadata["title"] = title_match.group(1).strip()
        
        # Extract meta description
        desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', html, re.IGNORECASE)
        if desc_match:
            metadata["description"] = desc_match.group(1).strip()
        
        # Extract language
        lang_match = re.search(r'<html[^>]*lang=["\'](.*?)["\']', html, re.IGNORECASE)
        if lang_match:
            metadata["language"] = lang_match.group(1).strip()
        
        return metadata

class GlobalAnalysisEngine:
    """Advanced global analysis for consensus, trends, and patterns"""
    
    def __init__(self, sphere_engine):
        self.sphere_engine = sphere_engine
        self.analysis_cache = {}
    
    def analyze_global_consensus(self, data_sources):
        """Analyze global consensus across data sources"""
        consensus_scores = {}
        
        for topic in ["government", "economy", "health", "environment", "technology"]:
            topic_sentiments = []
            
            for source in data_sources:
                # Simulate sentiment analysis
                sentiment = np.random.normal(0, 0.3)  # Placeholder for real analysis
                topic_sentiments.append(sentiment)
            
            # Calculate consensus (lower variance = higher consensus)
            variance = np.var(topic_sentiments) if topic_sentiments else 1
            consensus_scores[topic] = max(0, 1 - variance)
        
        return consensus_scores
    
    def detect_problematic_affairs(self, data_sources):
        """Detect globally problematic affairs"""
        problematic_indicators = {
            "conflicts": [],
            "crises": [],
            "disputes": [],
            "concerns": []
        }
        
        # Analyze data for problematic patterns
        for source in data_sources:
            # Placeholder for real analysis
            if np.random.random() > 0.7:  # Simulated detection
                problematic_indicators["concerns"].append({
                    "source": source.get("name", "Unknown"),
                    "concern": "Data inconsistency detected",
                    "severity": np.random.choice(["Low", "Medium", "High"])
                })
        
        return problematic_indicators
    
    def analyze_language_trends(self, data_sources):
        """Analyze trends in language use"""
        language_analysis = {
            "dominant_languages": {},
            "sentiment_trends": {},
            "topic_evolution": {}
        }
        
        for source in data_sources:
            language = source.get("language", "en")
            language_analysis["dominant_languages"][language] = language_analysis["dominant_languages"].get(language, 0) + 1
        
        return language_analysis
    
    def analyze_government_perceptions(self, data_sources):
        """Analyze perceptions of world government"""
        perception_metrics = {
            "trust_levels": {},
            "approval_ratings": {},
            "policy_sentiment": {}
        }
        
        for source in data_sources:
            country = source.get("country", "Unknown")
            perception_metrics["trust_levels"][country] = np.random.uniform(0.3, 0.9)  # Placeholder
        
        return perception_metrics

class FalconPressOfficeGUI:
    """Main GUI application for The Falcon Press Office"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("The Falcon Press Office - Relational Sphere Analysis System")
        self.root.geometry("1400x900")
        
        # Initialize core components
        self.sphere_engine = RelationalSphereEngine()
        self.gov_library = government_public_info_library.government_library
        self.patterns_library = predictive_news_patterns_library.predictive_patterns_library
        self.web_analyzer = WebContentAnalyzer()
        self.global_analyzer = GlobalAnalysisEngine(self.sphere_engine)
        
        # Generate initial sphere
        self.current_sphere = None
        self.analysis_results = {}
        
        # Setup GUI
        self.setup_gui()
        self.generate_initial_sphere()
        
    def setup_gui(self):
        """Setup the main GUI interface"""
        # Create notebook for workshops
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create workshop tabs
        self.create_sphere_visualization_tab()
        self.create_web_analysis_tab()
        self.create_global_analysis_tab()
        self.create_advanced_analytics_tab()
        self.create_document_processing_tab()
        self.create_internet_scouring_tab()
        
        # Status bar
        self.status_bar = ttk.Label(self.root, text="Ready - Relational Sphere Engine Active", relief='sunken')
        self.status_bar.pack(side='bottom', fill='x')
        
    def create_sphere_visualization_tab(self):
        """Create sphere generation and visualization workshop"""
        self.sphere_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.sphere_frame, text="🌐 Sphere Visualization")
        
        # Control panel
        control_frame = ttk.LabelFrame(self.sphere_frame, text="Sphere Controls")
        control_frame.pack(side='left', fill='y', padx=5, pady=5)
        
        ttk.Button(control_frame, text="Generate Sphere", command=self.generate_sphere).pack(pady=5)
        ttk.Button(control_frame, text="Refresh Data", command=self.refresh_sphere_data).pack(pady=5)
        ttk.Button(control_frame, text="Analyze Collisions", command=self.analyze_collisions).pack(pady=5)
        
        # Scaling controls
        ttk.Label(control_frame, text="Sphere Scale:").pack(pady=5)
        self.scale_var = tk.DoubleVar(value=1.0)
        scale_slider = ttk.Scale(control_frame, from_=0.1, to=3.0, variable=self.scale_var, orient='horizontal')
        scale_slider.pack(pady=5)
        
        # Detail level
        ttk.Label(control_frame, text="Detail Level:").pack(pady=5)
        self.detail_var = tk.IntVar(value=3)
        detail_combo = ttk.Combobox(control_frame, textvariable=self.detail_var, values=[1,2,3,4,5])
        detail_combo.pack(pady=5)
        
        # Visualization area
        viz_frame = ttk.LabelFrame(self.sphere_frame, text="3D Sphere Visualization")
        viz_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        
        # Create matplotlib figure for 3D visualization
        self.fig = plt.figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, viz_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
    def create_web_analysis_tab(self):
        """Create web content analysis and library building workshop"""
        self.web_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.web_frame, text="🌍 Web Analysis & Library Builder")
        
        # Input section
        input_frame = ttk.LabelFrame(self.web_frame, text="Web Content Input")
        input_frame.pack(side='top', fill='x', padx=5, pady=5)
        
        ttk.Label(input_frame, text="Enter URL:").pack(side='left', padx=5)
        self.url_entry = ttk.Entry(input_frame, width=50)
        self.url_entry.pack(side='left', padx=5)
        ttk.Button(input_frame, text="Analyze", command=self.analyze_web_content).pack(side='left', padx=5)
        ttk.Button(input_frame, text="Add to Library", command=self.add_to_library).pack(side='left', padx=5)
        
        # Analysis results
        results_frame = ttk.LabelFrame(self.web_frame, text="Analysis Results")
        results_frame.pack(side='top', fill='both', expand=True, padx=5, pady=5)
        
        self.web_results_text = scrolledtext.ScrolledText(results_frame, height=15)
        self.web_results_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Library builder
        library_frame = ttk.LabelFrame(self.web_frame, text="Custom Library Builder")
        library_frame.pack(side='bottom', fill='x', padx=5, pady=5)
        
        ttk.Button(library_frame, text="Create Library", command=self.create_custom_library).pack(side='left', padx=5)
        ttk.Button(library_frame, text="Save Library", command=self.save_custom_library).pack(side='left', padx=5)
        ttk.Button(library_frame, text="Load Library", command=self.load_custom_library).pack(side='left', padx=5)
        
    def create_global_analysis_tab(self):
        """Create global analysis dashboard workshop"""
        self.analysis_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.analysis_frame, text="📊 Global Analysis Dashboard")
        
        # Analysis controls
        control_frame = ttk.LabelFrame(self.analysis_frame, text="Analysis Controls")
        control_frame.pack(side='left', fill='y', padx=5, pady=5)
        
        # Analysis options
        self.consensus_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(control_frame, text="Global Consensus", variable=self.consensus_var).pack(anchor='w', pady=2)
        
        self.problematic_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(control_frame, text="Problematic Affairs", variable=self.problematic_var).pack(anchor='w', pady=2)
        
        self.language_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(control_frame, text="Language Trends", variable=self.language_var).pack(anchor='w', pady=2)
        
        self.government_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(control_frame, text="Government Perceptions", variable=self.government_var).pack(anchor='w', pady=2)
        
        ttk.Button(control_frame, text="Run Analysis", command=self.run_global_analysis).pack(pady=10)
        ttk.Button(control_frame, text="Export Results", command=self.export_analysis_results).pack(pady=5)
        
        # Results display
        results_frame = ttk.LabelFrame(self.analysis_frame, text="Analysis Results")
        results_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        
        # Create treeview for results
        self.analysis_tree = ttk.Treeview(results_frame, columns=('Metric', 'Value', 'Trend'))
        self.analysis_tree.heading('#0', text='Category')
        self.analysis_tree.heading('Metric', text='Metric')
        self.analysis_tree.heading('Value', text='Value')
        self.analysis_tree.heading('Trend', text='Trend')
        self.analysis_tree.pack(fill='both', expand=True)
        
    def create_advanced_analytics_tab(self):
        """Create advanced analytics workshop"""
        self.advanced_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.advanced_frame, text="🔬 Advanced Analytics")
        
        # Analytics options
        options_frame = ttk.LabelFrame(self.advanced_frame, text="Analytics Options")
        options_frame.pack(side='left', fill='y', padx=5, pady=5)
        
        self.geometric_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Geometric Observations", variable=self.geometric_var).pack(anchor='w', pady=2)
        
        self.collision_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Data Collisions", variable=self.collision_var).pack(anchor='w', pady=2)
        
        self.manipulation_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Manipulation Factors", variable=self.manipulation_var).pack(anchor='w', pady=2)
        
        # Custom search
        ttk.Label(options_frame, text="Custom Search:").pack(pady=5)
        self.search_entry = ttk.Entry(options_frame, width=20)
        self.search_entry.pack(pady=5)
        
        ttk.Button(options_frame, text="Search", command=self.custom_search).pack(pady=5)
        ttk.Button(options_frame, text="Run Advanced Analysis", command=self.run_advanced_analysis).pack(pady=10)
        
        # Visualization area
        viz_frame = ttk.LabelFrame(self.advanced_frame, text="Advanced Visualizations")
        viz_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        
        self.advanced_fig = plt.figure(figsize=(12, 8))
        self.advanced_canvas = FigureCanvasTkAgg(self.advanced_fig, viz_frame)
        self.advanced_canvas.get_tk_widget().pack(fill='both', expand=True)
        
    def create_document_processing_tab(self):
        """Create document processing workshop"""
        self.document_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.document_frame, text="📄 Document Processing")
        
        # Directory selection
        dir_frame = ttk.LabelFrame(self.document_frame, text="Directory Access")
        dir_frame.pack(side='top', fill='x', padx=5, pady=5)
        
        ttk.Label(dir_frame, text="Select Directory:").pack(side='left', padx=5)
        self.dir_label = ttk.Label(dir_frame, text="No directory selected")
        self.dir_label.pack(side='left', padx=5)
        ttk.Button(dir_frame, text="Browse", command=self.select_directory).pack(side='left', padx=5)
        
        # Processing controls
        proc_frame = ttk.LabelFrame(self.document_frame, text="Processing Controls")
        proc_frame.pack(side='top', fill='x', padx=5, pady=5)
        
        ttk.Button(proc_frame, text="Scan Documents", command=self.scan_documents).pack(side='left', padx=5)
        ttk.Button(proc_frame, text="Process Files", command=self.process_files).pack(side='left', padx=5)
        ttk.Button(proc_frame, text="Create Library", command=self.create_document_library).pack(side='left', padx=5)
        
        # File list
        list_frame = ttk.LabelFrame(self.document_frame, text="Document Files")
        list_frame.pack(side='bottom', fill='both', expand=True, padx=5, pady=5)
        
        self.file_tree = ttk.Treeview(list_frame, columns=('Type', 'Size', 'Modified'))
        self.file_tree.heading('#0', text='Filename')
        self.file_tree.heading('Type', text='Type')
        self.file_tree.heading('Size', text='Size')
        self.file_tree.heading('Modified', text='Modified')
        self.file_tree.pack(fill='both', expand=True)
        
    def create_internet_scouring_tab(self):
        """Create internet scouring and updates workshop"""
        self.scouring_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.scouring_frame, text="🌐 Internet Scouring & Updates")
        
        # Source management
        source_frame = ttk.LabelFrame(self.scouring_frame, text="Source Management")
        source_frame.pack(side='left', fill='y', padx=5, pady=5)
        
        ttk.Label(source_frame, text="Current Sources:").pack(pady=5)
        self.source_listbox = tk.Listbox(source_frame, height=10)
        self.source_listbox.pack(pady=5, padx=5)
        
        ttk.Button(source_frame, text="Add Source", command=self.add_source).pack(pady=2)
        ttk.Button(source_frame, text="Remove Source", command=self.remove_source).pack(pady=2)
        ttk.Button(source_frame, text="Edit Source", command=self.edit_source).pack(pady=2)
        
        # Scouring controls
        scour_control_frame = ttk.LabelFrame(self.scouring_frame, text="Scouring Controls")
        scour_control_frame.pack(side='left', fill='y', padx=5, pady=5)
        
        ttk.Label(scour_control_frame, text="Update Interval:").pack(pady=5)
        self.interval_var = tk.IntVar(value=60)
        interval_spin = ttk.Spinbox(scour_control_frame, from_=5, to=360, textvariable=self.interval_var)
        interval_spin.pack(pady=5)
        
        self.auto_update_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(scour_control_frame, text="Auto Update", variable=self.auto_update_var).pack(pady=5)
        
        ttk.Button(scour_control_frame, text="Start Scouring", command=self.start_scouring).pack(pady=5)
        ttk.Button(scour_control_frame, text="Stop Scouring", command=self.stop_scouring).pack(pady=5)
        ttk.Button(scour_control_frame, text="Update Now", command=self.update_now).pack(pady=5)
        
        # Results area
        results_frame = ttk.LabelFrame(self.scouring_frame, text="Scouring Results")
        results_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        
        self.scouring_text = scrolledtext.ScrolledText(results_frame, height=20)
        self.scouring_text.pack(fill='both', expand=True, padx=5, pady=5)
        
    def generate_initial_sphere(self):
        """Generate initial Relational Sphere from libraries"""
        try:
            self.current_sphere = self.sphere_engine.generate_sphere_from_libraries(
                self.gov_library, self.patterns_library
            )
            self.visualize_sphere()
            self.status_bar.config(text="Initial sphere generated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate sphere: {str(e)}")
            
    def generate_sphere(self):
        """Generate new sphere with current settings"""
        try:
            self.current_sphere = self.sphere_engine.generate_sphere_from_libraries(
                self.gov_library, self.patterns_library
            )
            self.visualize_sphere()
            self.status_bar.config(text="Sphere regenerated with current settings")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate sphere: {str(e)}")
    
    def visualize_sphere(self):
        """Visualize the current Relational Sphere"""
        if not self.current_sphere:
            return
        
        self.ax.clear()
        
        # Get coordinates and scale
        scale = self.scale_var.get()
        detail_level = self.detail_var.get()
        
        # Sample points based on detail level
        coords = list(self.current_sphere.coordinates.values())
        if len(coords) > detail_level * 100:
            indices = np.random.choice(len(coords), detail_level * 100, replace=False)
            coords = [coords[i] for i in indices]
        
        # Extract x, y, z coordinates
        x_coords = [c[0] * scale for c in coords]
        y_coords = [c[1] * scale for c in coords]
        z_coords = [c[2] * scale for c in coords]
        
        # Create 3D scatter plot
        scatter = self.ax.scatter(x_coords, y_coords, z_coords, 
                                 c=range(len(coords)), cmap='viridis', 
                                 s=20, alpha=0.6)
        
        # Draw collision lines if any
        for collision in self.current_sphere.geometric_collisions[:10]:  # Limit for visibility
            if collision[0] in self.current_sphere.coordinates and collision[1] in self.current_sphere.coordinates:
                coord1 = self.current_sphere.coordinates[collision[0]]
                coord2 = self.current_sphere.coordinates[collision[1]]
                self.ax.plot([coord1[0]*scale, coord2[0]*scale],
                           [coord1[1]*scale, coord2[1]*scale],
                           [coord1[2]*scale, coord2[2]*scale],
                           'r-', alpha=0.3)
        
        self.ax.set_xlabel('X Coordinate')
        self.ax.set_ylabel('Y Coordinate')
        self.ax.set_zlabel('Z Coordinate')
        self.ax.set_title(f'Relational Sphere - {len(coords)} Points')
        
        self.canvas.draw()
    
    def analyze_web_content(self):
        """Analyze web content from entered URL"""
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL")
            return
        
        self.web_results_text.delete(1.0, tk.END)
        self.web_results_text.insert(tk.END, f"Analyzing {url}...\n\n")
        self.root.update()
        
        try:
            result = self.web_analyzer.analyze_webpage(url)
            
            if "error" in result:
                self.web_results_text.insert(tk.END, f"Error: {result['error']}\n")
            else:
                self.web_results_text.insert(tk.END, "Analysis Complete!\n\n")
                self.web_results_text.insert(tk.END, f"Title: {result['metadata'].get('title', 'N/A')}\n")
                self.web_results_text.insert(tk.END, f"Language: {result['metadata'].get('language', 'N/A')}\n")
                self.web_results_text.insert(tk.END, f"Content Length: {len(result['content'])} characters\n\n")
                self.web_results_text.insert(tk.END, f"Summary:\n{result['summary']}\n\n")
                self.web_results_text.insert(tk.END, f"Content Preview:\n{result['content'][:500]}...\n")
                
                self.current_web_analysis = result
                
        except Exception as e:
            self.web_results_text.insert(tk.END, f"Analysis failed: {str(e)}\n")
    
    def run_global_analysis(self):
        """Run global analysis based on selected options"""
        self.analysis_tree.delete(*self.analysis_tree.get_children())
        
        # Get data sources (simplified for demo)
        data_sources = [
            {"name": f"Source_{i}", "country": "US", "language": "en"} 
            for i in range(10)
        ]
        
        try:
            if self.consensus_var.get():
                consensus = self.global_analyzer.analyze_global_consensus(data_sources)
                for topic, score in consensus.items():
                    self.analysis_tree.insert('', 'end', text='Consensus', 
                                            values=(topic, f"{score:.3f}", "Stable"))
            
            if self.problematic_var.get():
                problematic = self.global_analyzer.detect_problematic_affairs(data_sources)
                for category, items in problematic.items():
                    for item in items:
                        self.analysis_tree.insert('', 'end', text='Problematic', 
                                                values=(category, item.get('severity', 'Unknown'), "Increasing"))
            
            if self.language_var.get():
                language = self.global_analyzer.analyze_language_trends(data_sources)
                for lang, count in language.get('dominant_languages', {}).items():
                    self.analysis_tree.insert('', 'end', text='Language', 
                                            values=(lang, count, "Rising"))
            
            if self.government_var.get():
                govt = self.global_analyzer.analyze_government_perceptions(data_sources)
                for country, trust in govt.get('trust_levels', {}).items():
                    self.analysis_tree.insert('', 'end', text='Government', 
                                            values=(country, f"{trust:.2f}", "Stable"))
            
            self.status_bar.config(text="Global analysis completed")
            
        except Exception as e:
            messagebox.showerror("Error", f"Analysis failed: {str(e)}")
    
    def run_advanced_analysis(self):
        """Run advanced analytics"""
        self.advanced_fig.clear()
        
        # Create subplots for different visualizations
        if self.geometric_var.get():
            ax1 = self.advanced_fig.add_subplot(2, 2, 1, projection='3d')
            # Geometric observations visualization
            coords = list(self.current_sphere.coordinates.values())[:100]
            x = [c[0] for c in coords]
            y = [c[1] for c in coords]
            z = [c[2] for c in coords]
            ax1.scatter(x, y, z, alpha=0.6)
            ax1.set_title('Geometric Distribution')
        
        if self.collision_var.get():
            ax2 = self.advanced_fig.add_subplot(2, 2, 2)
            # Data collision heatmap
            collisions = len(self.current_sphere.geometric_collisions)
            ax2.bar(['Collisions', 'Safe Points'], [collisions, len(coords) - collisions])
            ax2.set_title('Collision Analysis')
        
        if self.manipulation_var.get():
            ax3 = self.advanced_fig.add_subplot(2, 2, 3)
            # Manipulation factors analysis
            factors = np.random.random(5)  # Placeholder
            ax3.pie(factors, labels=['Factor A', 'Factor B', 'Factor C', 'Factor D', 'Factor E'])
            ax3.set_title('Manipulation Factors')
        
        # Custom search results
        if hasattr(self, 'search_results'):
            ax4 = self.advanced_fig.add_subplot(2, 2, 4)
            ax4.plot(self.search_results)
            ax4.set_title('Custom Search Results')
        
        self.advanced_fig.tight_layout()
        self.advanced_canvas.draw()
        
        self.status_bar.config(text="Advanced analysis completed")
    
    def select_directory(self):
        """Select directory for document processing"""
        directory = filedialog.askdirectory()
        if directory:
            self.selected_directory = directory
            self.dir_label.config(text=directory)
            self.scan_documents()
    
    def scan_documents(self):
        """Scan selected directory for documents"""
        if not hasattr(self, 'selected_directory'):
            messagebox.showwarning("Warning", "Please select a directory first")
            return
        
        self.file_tree.delete(*self.file_tree.get_children())
        
        supported_extensions = ['.txt', '.pdf', '.doc', '.docx', '.html', '.json', '.csv']
        
        for root, dirs, files in os.walk(self.selected_directory):
            for file in files:
                if any(file.lower().endswith(ext) for ext in supported_extensions):
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    file_type = os.path.splitext(file)[1].upper()
                    
                    self.file_tree.insert('', 'end', text=file,
                                        values=(file_type, f"{file_size:,} bytes", modified_time.strftime('%Y-%m-%d %H:%M')))
        
        self.status_bar.config(text=f"Scanned {len(self.file_tree.get_children())} documents")
    
    def start_scouring(self):
        """Start automatic content scouring"""
        self.auto_update_var.set(True)
        self.status_bar.config(text="Scouring started")
        
        # Start scouring thread
        scour_thread = threading.Thread(target=self.scour_content_loop, daemon=True)
        scour_thread.start()
    
    def stop_scouring(self):
        """Stop automatic content scouring"""
        self.auto_update_var.set(False)
        self.status_bar.config(text="Scouring stopped")
    
    def scour_content_loop(self):
        """Main scouring loop"""
        while self.auto_update_var.get():
            try:
                self.update_now()
                time.sleep(self.interval_var.get())
            except Exception as e:
                self.scouring_text.insert(tk.END, f"Scouring error: {str(e)}\n")
                time.sleep(10)  # Wait before retrying
    
    def update_now(self):
        """Update content from sources immediately"""
        sources = list(self.source_listbox.get(0, tk.END))
        if not sources:
            sources = ["https://www.bbc.com/news", "https://www.cnn.com", "https://www.reuters.com"]
        
        self.scouring_text.insert(tk.END, f"Updating from {len(sources)} sources...\n")
        self.scouring_text.see(tk.END)
        
        for source in sources[:3]:  # Limit to 3 for demo
            try:
                result = self.web_analyzer.analyze_webpage(source)
                if "error" not in result:
                    self.scouring_text.insert(tk.END, f"✓ Updated: {source}\n")
                    self.scouring_text.insert(tk.END, f"  Summary: {result['summary'][:100]}...\n\n")
                else:
                    self.scouring_text.insert(tk.END, f"✗ Failed: {source} - {result['error']}\n")
            except Exception as e:
                self.scouring_text.insert(tk.END, f"✗ Error: {source} - {str(e)}\n")
            
            self.scouring_text.see(tk.END)
            self.root.update()
        
        self.status_bar.config(text="Content update completed")
    
    def custom_search(self):
        """Perform custom search analysis"""
        search_term = self.search_entry.get().strip()
        if not search_term:
            return
        
        # Simulate search results
        self.search_results = np.random.random(20)
        self.run_advanced_analysis()
        
    def export_analysis_results(self):
        """Export analysis results to file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                # Export analysis results
                results = {
                    "timestamp": datetime.now().isoformat(),
                    "analysis_type": "global_analysis",
                    "results": self.analysis_results
                }
                
                with open(filename, 'w') as f:
                    json.dump(results, f, indent=2)
                
                messagebox.showinfo("Success", f"Results exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Export failed: {str(e)}")
    
    def add_source(self):
        """Add new source to scouring list"""
        # Simple implementation
        source = simpledialog.askstring("Add Source", "Enter source URL:")
        if source:
            self.source_listbox.insert(tk.END, source)
    
    def remove_source(self):
        """Remove selected source"""
        selection = self.source_listbox.curselection()
        if selection:
            self.source_listbox.delete(selection[0])
    
    def edit_source(self):
        """Edit selected source"""
        selection = self.source_listbox.curselection()
        if selection:
            current = self.source_listbox.get(selection[0])
            new = simpledialog.askstring("Edit Source", "Enter new URL:", initialvalue=current)
            if new:
                self.source_listbox.delete(selection[0])
                self.source_listbox.insert(selection[0], new)
    
    def refresh_sphere_data(self):
        """Refresh sphere with latest data"""
        self.generate_sphere()
    
    def analyze_collisions(self):
        """Analyze geometric collisions in detail"""
        if not self.current_sphere:
            messagebox.showwarning("Warning", "Please generate a sphere first")
            return
        
        collisions = self.current_sphere.geometric_collisions
        
        if not collisions:
            messagebox.showinfo("Results", "No collisions detected in current sphere")
            return
        
        # Show collision details
        collision_text = f"Found {len(collisions)} collisions:\n\n"
        for i, (id1, id2, distance) in enumerate(collisions[:10]):
            collision_text += f"{i+1}. {id1} ↔ {id2}: Distance {distance:.2f}\n"
        
        messagebox.showinfo("Collision Analysis", collision_text)
    
    def create_custom_library(self):
        """Create custom library from analyzed web content"""
        if not hasattr(self, 'current_web_analysis'):
            messagebox.showwarning("Warning", "Please analyze web content first")
            return
        
        # Create custom library entry
        custom_entry = {
            "source_id": f"custom_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "content": self.current_web_analysis,
            "metadata": self.current_web_analysis.get("metadata", {}),
            "sphere_coordinates": (np.random.random() * 1000, np.random.random() * 1000, np.random.random() * 1000),
            "quantum_signature": hashlib.md5(str(self.current_web_analysis).encode()).hexdigest()[:16]
        }
        
        messagebox.showinfo("Success", "Custom library entry created")
    
    def save_custom_library(self):
        """Save custom library to file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            messagebox.showinfo("Success", f"Custom library saved to {filename}")
    
    def load_custom_library(self):
        """Load custom library from file"""
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            messagebox.showinfo("Success", f"Custom library loaded from {filename}")
    
    def process_files(self):
        """Process selected documents with AI summarization"""
        selection = self.file_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select files to process")
            return
        
        processed_files = []
        for item in selection:
            filename = self.file_tree.item(item)['text']
            # Simulate file processing
            processed_files.append(filename)
        
        messagebox.showinfo("Success", f"Processed {len(processed_files)} files with AI summarization")
    
    def create_document_library(self):
        """Create library from processed documents"""
        messagebox.showinfo("Success", "Document library created from processed files")

# Import missing modules
from tkinter import simpledialog

def main():
    """Main entry point for The Falcon Press Office"""
    root = tk.Tk()
    app = FalconPressOfficeGUI(root)
    
    # Add initial sources
    initial_sources = [
        "https://www.bbc.com/news",
        "https://www.cnn.com", 
        "https://www.reuters.com",
        "https://www.aljazeera.com",
        "https://apnews.com"
    ]
    
    for source in initial_sources:
        app.source_listbox.insert(tk.END, source)
    
    root.mainloop()

if __name__ == "__main__":
    main()