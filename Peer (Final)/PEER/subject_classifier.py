#!/usr/bin/env python3
"""
Subject Matter Classification System
Detects whether user input is within Peer's capabilities or out-of-scope
Handles classification of mathematical, scientific, and non-scientific content
"""

import re
from typing import Dict, List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass


class SubjectDomain(Enum):
    """Domains of knowledge"""
    MATHEMATICS = "Mathematics"
    PHYSICS = "Physics"
    CHEMISTRY = "Chemistry"
    BIOLOGY = "Biology"
    ENGINEERING = "Engineering"
    COMPUTER_SCIENCE = "Computer Science"
    STATISTICS = "Statistics"
    ECONOMICS = "Economics"
    OTHER_SCIENCE = "Other Science"
    HUMANITIES = "Humanities"
    SOCIAL_SCIENCE = "Social Science"
    EVERYDAY = "Everyday Topics"
    OUT_OF_SCOPE = "Out of Scope"
    UNKNOWN = "Unknown"


@dataclass
class ClassificationResult:
    """Result of subject matter classification"""
    domain: SubjectDomain
    confidence: float
    subcategories: List[str]
    warning_message: Optional[str] = None
    suggestions: List[str] = None


class SubjectClassifier:
    """
    Classifies user input into subject domains
    Detects out-of-scope content and provides guidance
    """
    
    def __init__(self):
        self.mathematical_keywords = self._init_mathematical_keywords()
        self.physics_keywords = self._init_physics_keywords()
        self.chemistry_keywords = self._init_chemistry_keywords()
        self.biology_keywords = self._init_biology_keywords()
        self.engineering_keywords = self._init_engineering_keywords()
        self.cs_keywords = self._init_cs_keywords()
        self.statistics_keywords = self._init_statistics_keywords()
        self.economics_keywords = self._init_economics_keywords()
        self.humanities_keywords = self._init_humanities_keywords()
        self.everyday_keywords = self._init_everyday_keywords()
    
    def _init_mathematical_keywords(self) -> List[str]:
        """Keywords indicating mathematical content"""
        return [
            'equation', 'formula', 'function', 'derivative', 'integral',
            'theorem', 'proof', 'calculus', 'algebra', 'geometry',
            'trigonometry', 'statistics', 'probability', 'matrix',
            'vector', 'tensor', 'series', 'limit', 'continuity',
            'differentiable', 'integrable', 'convergent', 'divergent',
            'polynomial', 'rational', 'exponential', 'logarithmic',
            'trigonometric', 'hyperbolic', 'complex', 'real',
            'imaginary', 'integer', 'rational number', 'irrational',
            'prime', 'composite', 'divisible', 'factor',
            'multiple', 'remainder', 'quotient', 'divisor',
            'numerator', 'denominator', 'fraction', 'decimal',
            'percentage', 'ratio', 'proportion', 'variable',
            'constant', 'parameter', 'coefficient', 'exponent',
            'power', 'root', 'square', 'cube', 'nth power',
            'logarithm', 'antilog', 'sine', 'cosine', 'tangent',
            'cotangent', 'secant', 'cosecant', 'arcsin', 'arccos',
            'arctan', 'hyperbolic', 'asymptote', 'parabola',
            'ellipse', 'hyperbola', 'circle', 'line', 'plane',
            'curve', 'surface', 'volume', 'area', 'perimeter',
            'circumference', 'radius', 'diameter', 'chord',
            'tangent line', 'secant line', 'slope', 'intercept',
            'vertex', 'focus', 'directrix', 'axis', 'origin',
            'coordinate', 'polar', 'cartesian', 'parametric',
            'implicit', 'explicit', 'differential equation',
            'partial differential equation', 'ordinary differential equation',
            'linear algebra', 'abstract algebra', 'number theory',
            'combinatorics', 'graph theory', 'topology', 'analysis',
            'optimization', 'numerical methods', 'approximation',
            'interpolation', 'extrapolation', 'regression', 'correlation',
            'variance', 'standard deviation', 'mean', 'median',
            'mode', 'expected value', 'probability distribution',
            'normal distribution', 'binomial', 'poisson', 'exponential',
            'gamma', 'beta', 'chi-square', 't-distribution',
            'f-distribution', 'uniform', 'continuous', 'discrete',
            'random variable', 'stochastic', 'deterministic',
            'chaotic', 'fractal', 'iteration', 'recursion',
            'induction', 'deduction', 'logic', 'set theory',
            'cardinality', 'ordinal', 'cardinal', 'infinite',
            'finite', 'countable', 'uncountable', 'bijection',
            'injection', 'surjection', 'isomorphism', 'homomorphism',
            'group', 'ring', 'field', 'vector space', 'metric space',
            'topological space', 'manifold', 'differentiable manifold',
            'riemannian', 'euclidean', 'non-euclidean', 'curvature',
            'geodesic', 'differential form', 'exterior derivative',
            'gradient', 'divergence', 'curl', 'laplacian', 'fourier',
            'laplace', 'transform', 'convolution', 'deconvolution',
            'filter', 'signal processing', 'wavelet', 'fractal',
            'dimension', 'fractal dimension', 'hausdorff dimension',
            'measure theory', 'lebesgue', 'riemann', 'stieltjes',
            'complex analysis', 'real analysis', 'functional analysis',
            'operator theory', 'spectral theory', 'harmonic analysis',
            'analytic number theory', 'algebraic number theory',
            'algebraic geometry', 'differential geometry', 'topology'
        ]
    
    def _init_physics_keywords(self) -> List[str]:
        """Keywords indicating physics content"""
        return [
            'force', 'mass', 'acceleration', 'velocity', 'speed',
            'momentum', 'energy', 'work', 'power', 'kinetic',
            'potential', 'gravity', 'gravitational', 'electric',
            'magnetic', 'electromagnetic', 'field', 'wave',
            'particle', 'quantum', 'relativity', 'special relativity',
            'general relativity', 'mechanics', 'classical mechanics',
            'quantum mechanics', 'thermodynamics', 'statistical mechanics',
            'electromagnetism', 'optics', 'acoustics', 'fluid dynamics',
            'solid state physics', 'condensed matter', 'nuclear physics',
            'particle physics', 'astrophysics', 'cosmology',
            'atomic physics', 'molecular physics', 'biophysics',
            'geophysics', 'atmospheric physics', 'plasma physics',
            'laser', 'photon', 'electron', 'proton', 'neutron',
            'atom', 'molecule', 'crystal', 'lattice', 'band structure',
            'semiconductor', 'superconductor', 'magnetism', 'superconductivity',
            'phase transition', 'critical point', 'entropy', 'enthalpy',
            'temperature', 'pressure', 'volume', 'heat', 'temperature',
            'kelvin', 'celsius', 'fahrenheit', 'thermometer',
            'calorimetry', 'heat engine', 'carnot', 'efficiency',
            'first law', 'second law', 'third law', 'zeroth law',
            'ideal gas', 'real gas', 'van der waals', 'boltzmann',
            'maxwell-boltzmann', 'fermi-dirac', 'bose-einstein',
            'schrodinger', 'heisenberg', 'uncertainty principle',
            'wave function', 'operator', 'eigenvalue', 'eigenvector',
            'hamiltonian', 'lagrangian', 'action', 'principle',
            'least action', 'noether', 'symmetry', 'conservation',
            'momentum conservation', 'energy conservation', 'angular momentum',
            'angular velocity', 'angular acceleration', 'torque',
            'moment of inertia', 'center of mass', 'center of gravity',
            'equilibrium', 'statics', 'dynamics', 'kinematics',
            'kinetics', 'oscillation', 'vibration', 'resonance',
            'damping', 'driven oscillator', 'coupled oscillator',
            'wave equation', 'heat equation', 'diffusion equation',
            'laplace equation', 'poisson equation', 'maxwell equations',
            'gauss law', 'faraday law', 'ampere law', 'lenz law',
            'electric field', 'magnetic field', 'electric potential',
            'voltage', 'current', 'resistance', 'capacitance',
            'inductance', 'impedance', 'admittance', 'reactance',
            'circuit', 'series', 'parallel', 'ohm', 'kirchhoff',
            'thevenin', 'norton', 'millman', 'superposition',
            'frequency', 'wavelength', 'period', 'amplitude',
            'phase', 'interference', 'diffraction', 'reflection',
            'refraction', 'polarization', 'dispersion', 'absorption',
            'emission', 'scattering', 'rayleigh', 'compton',
            'photoelectric', 'doppler', 'redshift', 'blueshift',
            'big bang', 'expansion', 'hubble', 'cosmic microwave',
            'black hole', 'event horizon', 'singularity', 'neutron star',
            'pulsar', 'quasar', 'galaxy', 'star', 'planet',
            'orbit', 'trajectory', 'escape velocity', 'orbital mechanics',
            'rocket', 'propulsion', 'thrust', 'specific impulse',
            'delta v', 'orbital velocity', 'geostationary', 'escape',
            'gravity assist', 'hohmann', 'transfer', 'trajectory'
        ]
    
    def _init_chemistry_keywords(self) -> List[str]:
        """Keywords indicating chemistry content"""
        return [
            'molecule', 'atom', 'element', 'compound', 'mixture',
            'solution', 'suspension', 'colloid', 'reaction', 'catalyst',
            'enzyme', 'acid', 'base', 'ph', 'redox', 'oxidation',
            'reduction', 'oxidation state', 'valence', 'electron',
            'proton', 'neutron', 'nucleus', 'orbital', 'shell',
            'subshell', 'quantum number', 'periodic table', 'group',
            'period', 'metal', 'nonmetal', 'metalloid', 'transition',
            'alkali', 'alkaline earth', 'halogen', 'noble gas',
            'lanthanide', 'actinide', 'ionic', 'covalent', 'metallic',
            'bond', 'bond length', 'bond angle', 'bond energy',
            'hybridization', 'resonance', 'isomer', 'structural isomer',
            'geometric isomer', 'optical isomer', 'enantiomer', 'diastereomer',
            'stereochemistry', 'chirality', 'racemic', 'optical activity',
            'polar', 'nonpolar', 'dipole', 'hydrogen bond', 'van der waals',
            'london dispersion', 'dipole-dipole', 'ion-dipole', 'solvation',
            'hydration', 'solvation energy', 'lattice energy', 'born-haber',
            'enthalpy', 'entropy', 'gibbs free energy', 'spontaneous',
            'equilibrium', 'dynamic equilibrium', 'le chatelier', 'reaction quotient',
            'equilibrium constant', 'rate', 'rate law', 'order', 'molecularity',
            'activation energy', 'catalysis', 'enzyme kinetics', 'michaelis-menten',
            'arrhenius', 'collision theory', 'transition state', 'mechanism',
            'intermediate', 'elementary step', 'rate determining', 'kinetics',
            'thermodynamics', 'first law', 'second law', 'third law',
            'heat of formation', 'heat of reaction', 'calorimetry',
            'bomb calorimeter', 'coffee cup', 'hess law', 'born-haber cycle',
            'gibbs-helmholtz', 'clausius-clapeyron', 'phase diagram',
            'triple point', 'critical point', 'supercritical', 'sublimation',
            'deposition', 'vaporization', 'condensation', 'freezing',
            'melting', 'boiling', 'heat capacity', 'specific heat',
            'molar heat capacity', 'ideal gas', 'real gas', 'van der waals',
            'gas laws', 'boyle', 'charles', 'gay-lussac', 'avogadro',
            'dalton', 'henry', 'raoult', 'colligative', 'boiling point',
            'freezing point', 'osmotic pressure', 'vapor pressure',
            'solutions', 'solubility', 'solute', 'solvent', 'concentration',
            'molarity', 'molality', 'mole fraction', 'mass percent',
            'volume percent', 'parts per million', 'parts per billion',
            'titration', 'indicator', 'endpoint', 'equivalence point',
            'acid-base', 'redox', 'complexometric', 'precipitation',
            'analytical', 'qualitative', 'quantitative', 'spectroscopy',
            'chromatography', 'electrophoresis', 'mass spectrometry',
            'nuclear magnetic resonance', 'infrared', 'ultraviolet',
            'visible', 'x-ray', 'atomic absorption', 'atomic emission',
            'flame', 'gravimetric', 'volumetric', 'electrochemical',
            'potentiometric', 'voltammetric', 'amperometric', 'conductometric',
            'organic', 'inorganic', 'analytical', 'physical', 'biochemistry',
            'polymer', 'materials', 'environmental', 'medicinal',
            'pharmaceutical', 'industrial', 'agricultural', 'forensic'
        ]
    
    def _init_biology_keywords(self) -> List[str]:
        """Keywords indicating biology content"""
        return [
            'cell', 'organism', 'species', 'genetics', 'dna', 'rna',
            'protein', 'enzyme', 'metabolism', 'photosynthesis', 'respiration',
            'ecosystem', 'evolution', 'natural selection', 'mutation',
            'gene', 'chromosome', 'allele', 'dominant', 'recessive',
            'genotype', 'phenotype', 'heredity', 'inheritance', 'mendelian',
            'mitosis', 'meiosis', 'cell division', 'cell cycle',
            'interphase', 'prophase', 'metaphase', 'anaphase', 'telophase',
            'cytokinesis', 'tissue', 'organ', 'organ system', 'homeostasis',
            'physiology', 'anatomy', 'morphology', 'taxonomy', 'classification',
            'kingdom', 'phylum', 'class', 'order', 'family', 'genus',
            'species', 'bacteria', 'archaea', 'eukarya', 'prokaryote',
            'eukaryote', 'virus', 'prion', 'viroid', 'plant', 'animal',
            'fungi', 'protist', 'microorganism', 'microbe', 'bacteria',
            'virus', 'fungus', 'protozoa', 'algae', 'parasite',
            'pathogen', 'immune system', 'antibody', 'antigen', 'vaccine',
            'infection', 'disease', 'epidemic', 'pandemic', 'virology',
            'bacteriology', 'mycology', 'parasitology', 'immunology',
            'epidemiology', 'public health', 'medicine', 'pharmacology',
            'toxicology', 'pharmacokinetics', 'pharmacodynamics', 'drug',
            'medication', 'therapy', 'treatment', 'diagnosis', 'prognosis',
            'symptom', 'sign', 'syndrome', 'disorder', 'condition',
            'cancer', 'tumor', 'malignant', 'benign', 'metastasis',
            'carcinogen', 'mutagen', 'teratogen', 'oncology', 'cardiology',
            'neurology', 'endocrinology', 'gastroenterology', 'nephrology',
            'pulmonology', 'dermatology', 'ophthalmology', 'otolaryngology',
            'orthopedics', 'surgery', 'anesthesiology', 'radiology',
            'pathology', 'laboratory', 'clinical', 'biochemistry',
            'molecular biology', 'cell biology', 'developmental biology',
            'embryology', 'comparative anatomy', 'comparative physiology',
            'ethology', 'animal behavior', 'sociobiology', 'population',
            'community', 'ecology', 'ecosystem', 'biome', 'biosphere',
            'biodiversity', 'conservation', 'endangered', 'extinct',
            'extinction', 'habitat', 'niche', 'trophic level', 'food chain',
            'food web', 'energy flow', 'nutrient cycling', 'carbon cycle',
            'nitrogen cycle', 'phosphorus cycle', 'water cycle', 'biogeochemical',
            'succession', 'primary', 'secondary', 'climax', 'pioneer',
            'keystone', 'invasive', 'native', 'introduced', 'exotic',
            'pollution', 'climate change', 'global warming', 'ocean acidification',
            'deforestation', 'desertification', 'urbanization', 'agriculture',
            'farming', 'fisheries', 'aquaculture', 'forestry', 'wildlife',
            'conservation biology', 'restoration ecology', 'landscape ecology',
            'marine biology', 'freshwater biology', 'terrestrial ecology',
            'microbial ecology', 'soil ecology', 'plant ecology', 'animal ecology',
            'behavioral ecology', 'evolutionary ecology', 'population ecology',
            'community ecology', 'ecosystem ecology'
        ]
    
    def _init_engineering_keywords(self) -> List[str]:
        """Keywords indicating engineering content"""
        return [
            'beam', 'column', 'foundation', 'concrete', 'steel',
            'stress', 'strain', 'load', 'material', 'fatigue',
            'corrosion', 'friction', 'lubrication', 'sensor', 'actuator',
            'control', 'feedback', 'circuit', 'voltage', 'current',
            'prototype', 'validation', 'verification', 'quality', 'reliability',
            'heat transfer', 'fluid dynamics', 'vibration', 'acoustics',
            'signal processing', 'communication', 'protocol', 'firmware',
            'embedded', 'real-time', 'cybersecurity', 'attack', 'vulnerability',
            'malware', 'firewall', 'intrusion', 'robotics', 'automation',
            'autonomous', 'drone', 'manipulator', 'gripper', 'path planning',
            'navigation', 'slam', 'lidar', 'radar', 'sonar',
            'satellite', 'gps', 'positioning', 'photogrammetry', 'imagery',
            'codec', 'compression', 'bandwidth', 'latency', 'throughput',
            'quality of service', 'uptime', 'availability', 'scalability'
        ]
    
    def _init_cs_keywords(self) -> List[str]:
        """Keywords indicating computer science content"""
        return [
            'algorithm', 'data structure', 'array', 'linked list', 'stack',
            'queue', 'tree', 'graph', 'hash table', 'heap',
            'priority queue', 'binary tree', 'binary search tree', 'b-tree',
            'trie', 'depth-first', 'breadth-first', 'dijkstra', 'floyd-warshall',
            'bellman-ford', 'prim', 'kruskal', 'topological',
            'traveling salesman', 'knapsack', 'bin packing', 'scheduling',
            'dynamic programming', 'greedy', 'backtracking', 'branch and bound',
            'neural network', 'deep learning', 'machine learning',
            'supervised', 'unsupervised', 'reinforcement',
            'classification', 'regression', 'clustering', 'cnn', 'rnn',
            'lstm', 'transformer', 'attention', 'bert', 'gpt',
            'nlp', 'computer vision', 'object detection', 'segmentation',
            'sentiment', 'named entity', 'parsing', 'tagging',
            'word embedding', 'word2vec', 'glove', 'fine-tuning',
            'transfer learning', 'gpu', 'tpu', 'quantum computing',
            'qubit', 'shor', 'grover', 'python', 'java',
            'javascript', 'typescript', 'c++', 'rust', 'go',
            'sql', 'nosql', 'mongodb', 'redis', 'neo4j',
            'acid', 'cap', 'base', 'sharding', 'indexing',
            'agile', 'scrum', 'kanban', 'devops', 'ci/cd',
            'kubernetes', 'docker', 'microservice', 'serverless',
            'aws', 'azure', 'gcp', 'api', 'rest', 'graphql',
            'webhook', 'http', 'https', 'tcp', 'udp', 'ip',
            'cryptography', 'encryption', 'blockchain', 'bitcoin', 'ethereum'
        ]
    
    def _init_statistics_keywords(self) -> List[str]:
        """Keywords indicating statistics content"""
        return [
            'mean', 'median', 'mode', 'variance', 'standard deviation',
            'covariance', 'correlation', 'regression', 'linear', 'logistic',
            'polynomial', 'multiple', 'multivariate', 'hypothesis', 'test',
            'null', 'alternative', 'p-value', 'significance', 'confidence',
            'interval', 'level', 'alpha', 'beta', 'power', 'sample',
            'size', 'population', 'parameter', 'statistic', 'estimator',
            'estimate', 'bias', 'variance', 'mean squared error', 'efficiency',
            'consistency', 'sufficiency', 'completeness', 'likelihood', 'maximum',
            'bayesian', 'prior', 'posterior', 'marginal', 'conditional',
            'joint', 'distribution', 'probability', 'density', 'mass',
            'function', 'cumulative', 'quantile', 'percentile', 'quartile',
            'interquartile', 'range', 'outlier', 'skewness', 'kurtosis',
            'moment', 'central', 'raw', 'normal', 'gaussian',
            'standard normal', 'z-score', 't-distribution', 'chi-square',
            'f-distribution', 'binomial', 'poisson', 'exponential', 'gamma',
            'beta', 'uniform', 'geometric', 'negative binomial', 'hypergeometric',
            'multinomial', 'dirichlet', 'multivariate normal', 'multivariate t',
            'wishart', 'inverse wishart', 'sampling', 'random', 'pseudo-random',
            'monte carlo', 'bootstrap', 'jackknife', 'cross-validation',
            'resampling', 'permutation', 'anova', 'anova', 'ancova',
            'manova', 'repeated measures', 'mixed effects', 'random effects',
            'fixed effects', 'nested', 'factorial', 'latin square', 'block',
            'design of experiments', 'doe', 'factorial', 'fractional',
            'response surface', 'optimal', 'taguchi', 'six sigma',
            'quality control', 'control chart', 'shewhart', 'cusum', 'ewma',
            'process capability', 'cpk', 'ppk', 'specification', 'tolerance',
            'measurement system', 'gage r&r', 'repeatability', 'reproducibility',
            'uncertainty', 'precision', 'accuracy', 'trueness', 'validity',
            'reliability', 'survival', 'censoring', 'kaplan-meier', 'cox',
            'proportional hazards', 'log-rank', 'life table', 'hazard',
            'survival function', 'cumulative hazard', 'time series', 'trend',
            'seasonality', 'cycle', 'autocorrelation', 'partial autocorrelation',
            'stationary', 'non-stationary', 'unit root', 'arima', 'sarima',
            'arch', 'garch', 'var', 'vecm', 'cointegration',
            'forecast', 'prediction', 'exponential smoothing', 'holt-winters',
            'neural network', 'machine learning', 'clustering', 'k-means',
            'hierarchical', 'dbscan', 'mixture', 'gaussian mixture', 'em',
            'expectation-maximization', 'pca', 'principal component', 'factor',
            'analysis', 'canonical correlation', 'discriminant', 'multidimensional',
            'scaling', 'mds', 'tsne', 'umap', 'cluster analysis',
            'classification', 'logistic', 'discriminant', 'knn', 'decision tree',
            'random forest', 'svm', 'naive bayes', 'neural', 'deep',
            'ensemble', 'bagging', 'boosting', 'gradient boosting', 'xgboost',
            'lightgbm', 'catboost', 'evaluation', 'accuracy', 'precision',
            'recall', 'f1', 'roc', 'auc', 'confusion matrix',
            'sensitivity', 'specificity', 'positive predictive', 'negative predictive',
            'likelihood ratio', 'odds ratio', 'risk ratio', 'hazard ratio',
            'relative risk', 'absolute risk', 'number needed', 'diagnostic',
            'screening', 'epidemiology', 'cohort', 'case-control', 'cross-sectional',
            'ecological', 'meta-analysis', 'systematic review', 'publication',
            'bias', 'selection bias', 'information bias', 'confounding',
            'effect modification', 'interaction', 'causality', 'counterfactual',
            'propensity score', 'instrumental variable', 'difference-in-differences',
            'regression discontinuity', 'synthetic control', 'matching', 'weighting',
            'survey', 'sampling', 'stratified', 'cluster', 'systematic',
            'convenience', 'quota', 'snowball', 'non-probability', 'questionnaire',
            'interview', 'focus group', 'observation', 'experiment', 'rct',
            'randomized controlled trial', 'blinding', 'placebo', 'intention',
            'to treat', 'per protocol', 'as treated', 'subgroup', 'sensitivity'
        ]
    
    def _init_economics_keywords(self) -> List[str]:
        """Keywords indicating economics content"""
        return [
            'supply', 'demand', 'price', 'market', 'equilibrium',
            'elasticity', 'utility', 'preference', 'consumer', 'producer',
            'surplus', 'cost', 'revenue', 'profit', 'loss',
            'marginal', 'average', 'total', 'fixed', 'variable',
            'opportunity', 'sunk', 'production', 'function', 'isoquant',
            'indifference', 'budget constraint', 'optimization', 'substitution',
            'income', 'slutsky', 'hicks', 'compensated', 'uncompensated',
            'welfare', 'deadweight', 'tax', 'subsidy', 'tariff',
            'quota', 'price control', 'minimum wage', 'rent control',
            'monopoly', 'oligopoly', 'monopolistic', 'perfect', 'competition',
            'game theory', 'nash', 'dominant', 'prisoner', 'bertrand',
            'cournot', 'stackelberg', 'collusion', 'cartel', 'price',
            'discrimination', 'bargaining', 'auction', 'mechanism', 'design',
            'principal-agent', 'adverse', 'selection', 'moral', 'hazard',
            'signaling', 'screening', 'information', 'asymmetric', 'externalities',
            'public', 'goods', 'common', 'resources', 'free',
            'rider', 'tragedy', 'commons', 'coase', 'pigouvian',
            'microeconomics', 'macroeconomics', 'gdp', 'gnp', 'inflation',
            'unemployment', 'recession', 'depression', 'growth', 'business',
            'cycle', 'fiscal', 'monetary', 'policy', 'central',
            'bank', 'interest', 'rate', 'exchange', 'money',
            'supply', 'demand', 'liquidity', 'multiplier', 'keynesian',
            'classical', 'monetarist', 'new', 'keynesian', 'real',
            'business', 'cycle', 'phillips', 'curve', 'aggregate',
            'demand', 'supply', 'is-lm', 'ad-as', ' mundell-fleming',
            'open', 'economy', 'balance', 'payments', 'current',
            'account', 'capital', 'account', 'trade', 'surplus',
            'deficit', 'devaluation', 'appreciation', 'fixed', 'flexible',
            'exchange', 'regime', 'gold', 'standard', 'breton',
            'woods', 'international', 'finance', 'development', 'economics',
            'poverty', 'inequality', 'gini', 'lorenz', 'human',
            'development', 'institutional', 'behavioral', 'experimental',
            'neuroeconomics', 'econometrics', 'regression', 'time', 'series',
            'panel', 'data', 'cross-section', 'endogeneity', 'instrument',
            'identification', 'causality', 'counterfactual', 'difference',
            'in-differences', 'regression', 'discontinuity', 'synthetic',
            'control', 'propensity', 'score', 'matching', 'labor',
            'economics', 'labor', 'market', 'wage', 'employment',
            'unemployment', 'participation', 'human', 'capital', 'education',
            'training', 'discrimination', 'minimum', 'wage', 'union',
            'collective', 'bargaining', 'public', 'economics', 'public',
            'choice', 'social', 'welfare', 'cost-benefit', 'voting',
            'mechanism', 'arrow', 'impossibility', 'condorcet', 'median',
            'voter', 'bureaucracy', 'regulation', 'deregulation', 'privatization',
            'nationalization', 'industrial', 'organization', 'strategy',
        ]
    
    def _init_humanities_keywords(self) -> List[str]:
        """Keywords indicating humanities content (OUT OF SCOPE)"""
        return [
            'literature', 'novel', 'poem', 'poetry', 'story', 'fiction',
            'non-fiction', 'essay', 'article', 'journalism', 'news',
            'politics', 'government', 'election', 'vote', 'democracy',
            'republic', 'monarchy', 'dictatorship', 'communism', 'socialism',
            'capitalism', 'liberalism', 'conservatism', 'fascism', 'anarchism',
            'ideology', 'political party', 'campaign', 'policy',
            'law', 'legal', 'court', 'judge', 'lawyer', 'attorney',
            'case', 'verdict', 'guilty', 'innocent', 'trial', 'jury',
            'constitution', 'amendment', 'statute', 'regulation', 'compliance',
            'contract', 'tort', 'criminal', 'civil', 'diplomacy', 'treaty',
            'war', 'peace', 'conflict', 'military', 'army', 'navy',
            'air force', 'weapon', 'soldier', 'general', 'admiral',
            'battle', 'strategy', 'tactics', 'history', 'historical',
            'ancient', 'medieval', 'modern', 'contemporary', 'century',
            'decade', 'era', 'period', 'civilization', 'culture',
            'religion', 'faith', 'belief', 'god', 'spiritual', 'church',
            'temple', 'mosque', 'synagogue', 'pray', 'worship',
            'scripture', 'bible', 'quran', 'torah', 'veda',
            'philosophy', 'philosophical', 'ethics', 'morality', 'moral',
            'virtue', 'value', 'principle', 'existential', 'phenomenology',
            'metaphysics', 'epistemology', 'aesthetics', 'art',
            'music', 'painting', 'sculpture', 'film', 'movie',
            'theater', 'drama', 'comedy', 'tragedy', 'performance',
            'dance', 'choreography', 'composition', 'criticism', 'review',
            'critique', 'interpretation', 'theory', 'methodology',
            'hermeneutics', 'deconstruction', 'postmodern', 'modernist',
            'romantic', 'classical', 'baroque', 'renaissance', 'gothic',
            'byzantine', 'prehistoric', 'anthropology', 'sociology',
            'psychology', 'social', 'cultural', 'gender', 'race',
            'ethnicity', 'class', 'identity', 'feminism', 'marxism',
            'postcolonial', 'queer', 'media', 'journalism', 'communication',
            'advertising', 'marketing', 'brand', 'consumer', 'entertainment',
            'celebrity', 'gossip', 'tabloid', 'magazine', 'blog',
            'podcast', 'vlog', 'influencer', 'gaming', 'esports',
            'sports', 'football', 'basketball', 'baseball', 'soccer',
            'tennis', 'golf', 'hockey', 'swimming', 'olympics',
            'championship', 'league', 'team', 'player', 'coach', 'manager',
            'owner', 'fan', 'supporter', 'spectator', 'audience', 'ticket',
            'venue', 'stadium', 'arena'
        ]
    
    def _init_everyday_keywords(self) -> List[str]:
        """Keywords indicating everyday topics (OUT OF SCOPE)"""
        return [
            'weather', 'forecast', 'rain', 'recipe', 'cook', 'bake',
            'food', 'meal', 'restaurant', 'cafe', 'bar', 'pub',
            'grocery', 'shopping', 'store', 'market', 'mall',
            'discount', 'sale', 'coupon', 'delivery', 'return', 'refund',
            'travel', 'vacation', 'trip', 'holiday', 'flight', 'hotel',
            'booking', 'destination', 'beach', 'mountain', 'sightseeing',
            'car', 'drive', 'vehicle', 'bus', 'train', 'taxi',
            'uber', 'lyft', 'exercise', 'gym', 'fitness',
            'doctor', 'hospital', 'clinic', 'medicine', 'pharmacy',
            'prescription', 'symptom', 'headache', 'fever', 'cold', 'flu',
            'cough', 'stomach', 'nausea', 'vomiting', 'insurance',
            'rent', 'mortgage', 'loan', 'credit', 'debt', 'bank',
            'account', 'savings', 'investment', 'stock', 'bond', 'fund',
            'retirement', 'pension', 'social security', 'tax', 'income',
            'file', 'return', 'deduction', 'job', 'work', 'career',
            'employment', 'resume', 'interview', 'salary', 'wage', 'bonus',
            'promotion', 'raise', 'benefit', 'vacation', 'sick', 'leave',
            'family', 'parent', 'child', 'baby', 'kid', 'teen',
            'grandparent', 'sibling', 'spouse', 'husband', 'wife', 'partner',
            'friend', 'relationship', 'dating', 'marriage', 'divorce',
            'wedding', 'anniversary', 'birthday', 'party', 'celebration',
            'christmas', 'thanksgiving', 'halloween', 'easter', 'new year',
            'pet', 'dog', 'cat', 'bird', 'fish', 'vet',
            'hobby', 'interest', 'craft', 'diy', 'garden', 'plant',
            'flower', 'tree', 'lawn', 'clean', 'house', 'repair',
            'appliance', 'furniture', 'decor', 'paint', 'wall'
        ]
    
    def classify(self, text: str) -> ClassificationResult:
        """
        Classify input text into subject domains
        
        Args:
            text: Input text to classify
            
        Returns:
            ClassificationResult with domain, confidence, and warnings
        """
        text_lower = text.lower()
        
        # Check for explicit formula patterns first (highest priority)
        formula_patterns = [
            r'[a-z]\s*=\s*',  # variable = something
            r'\b[sin|cos|tan|log|ln|sqrt|exp]\s*\(',  # mathematical functions
            r'[a-z]\s*[\^]\s*\d+',  # exponent like x^2
            r'[∂|∫|∑|∏|√]',  # mathematical symbols
            r'\b\d+\s*[a-z]',  # number followed by variable
            r'[a-z]\s*[+\-*/]\s*[a-z]',  # variable operation variable
            r'[a-z]\s*[\+\-\*\/\^]\s*\(',  # operation with parentheses
            r'\b(d|dy|dx|dz|d[sxyz])\s*/\s*(d|dy|dx|dz|d[sxyz])',  # derivatives
        ]
        
        has_formula = any(re.search(pattern, text_lower, re.IGNORECASE) for pattern in formula_patterns)
        
        # Check for mathematical/scientific terms
        sci_math_domains = [
            SubjectDomain.MATHEMATICS, SubjectDomain.PHYSICS, SubjectDomain.CHEMISTRY,
            SubjectDomain.BIOLOGY, SubjectDomain.ENGINEERING, SubjectDomain.COMPUTER_SCIENCE,
            SubjectDomain.STATISTICS, SubjectDomain.ECONOMICS
        ]
        
        out_of_scope_domains = [SubjectDomain.HUMANITIES, SubjectDomain.EVERYDAY]
        
        # Count keyword matches for each domain
        scores = {
            SubjectDomain.MATHEMATICS: self._count_matches(text_lower, self.mathematical_keywords),
            SubjectDomain.PHYSICS: self._count_matches(text_lower, self.physics_keywords),
            SubjectDomain.CHEMISTRY: self._count_matches(text_lower, self.chemistry_keywords),
            SubjectDomain.BIOLOGY: self._count_matches(text_lower, self.biology_keywords),
            SubjectDomain.ENGINEERING: self._count_matches(text_lower, self.engineering_keywords),
            SubjectDomain.COMPUTER_SCIENCE: self._count_matches(text_lower, self.cs_keywords),
            SubjectDomain.STATISTICS: self._count_matches(text_lower, self.statistics_keywords),
            SubjectDomain.ECONOMICS: self._count_matches(text_lower, self.economics_keywords),
            SubjectDomain.HUMANITIES: self._count_matches(text_lower, self.humanities_keywords),
            SubjectDomain.EVERYDAY: self._count_matches(text_lower, self.everyday_keywords)
        }
        
        # If has formula pattern, prioritize sci/math domains
        if has_formula:
            # Zero out out-of-scope scores if formula detected
            for domain in out_of_scope_domains:
                scores[domain] = 0
        
        # Find highest scoring domain
        max_score = max(scores.values())
        
        # If no matches, return unknown
        if max_score == 0:
            return ClassificationResult(
                domain=SubjectDomain.UNKNOWN,
                confidence=0.0,
                subcategories=[],
                warning_message="Unable to classify input. Please provide more context.",
                suggestions=["Provide a formula or mathematical expression", "Describe a scientific concept", "Ask about physics, chemistry, or engineering"]
            )
        
        # Get best domain(s)
        best_domains = [domain for domain, score in scores.items() if score == max_score]
        best_domain = best_domains[0]
        
        # Special handling: if there's a formula but best domain is out-of-scope, 
        # default to mathematics
        if has_formula and best_domain in out_of_scope_domains:
            best_domain = SubjectDomain.MATHEMATICS
        
        # Calculate confidence
        total_matches = sum(scores.values())
        confidence = max_score / total_matches if total_matches > 0 else 0.0
        
        # Determine subcategories
        subcategories = self._get_subcategories(text_lower, best_domain)
        
        # Generate warning if out of scope
        warning_message = None
        suggestions = []
        
        if best_domain in [SubjectDomain.HUMANITIES, SubjectDomain.EVERYDAY]:
            warning_message = f"Your input appears to be about {best_domain.value.lower()}, which is outside Peer's scope. Peer is designed for mathematical and scientific formulas and analysis."
            suggestions = [
                "If you have a mathematical formula, please enter it directly",
                "For scientific questions, provide the relevant formula or equation",
                "Peer can help with physics, chemistry, engineering, mathematics, statistics, economics, biology, and computer science",
                "Consider rephrasing your input to include mathematical or scientific content"
            ]
        elif best_domain in [SubjectDomain.MATHEMATICS, SubjectDomain.PHYSICS, 
                            SubjectDomain.CHEMISTRY, SubjectDomain.BIOLOGY,
                            SubjectDomain.ENGINEERING, SubjectDomain.COMPUTER_SCIENCE,
                            SubjectDomain.STATISTICS, SubjectDomain.ECONOMICS]:
            suggestions = [
                f"Great! Your input is related to {best_domain.value.lower()}.",
                "Peer can help analyze formulas and validate results in this domain.",
                "You can enter formulas using standard mathematical notation.",
                "Use the 'Stuck' button if you need help entering your formula."
            ]
        
        return ClassificationResult(
            domain=best_domain,
            confidence=confidence,
            subcategories=subcategories,
            warning_message=warning_message,
            suggestions=suggestions
        )
    
    def _count_matches(self, text: str, keywords: List[str]) -> int:
        """Count keyword matches in text"""
        count = 0
        for keyword in keywords:
            if keyword.lower() in text:
                count += 1
        return count
    
    def _get_subcategories(self, text: str, domain: SubjectDomain) -> List[str]:
        """Get subcategories for the domain"""
        subcategories = []
        text_lower = text.lower()
        
        # Domain-specific subcategory detection
        if domain == SubjectDomain.MATHEMATICS:
            if any(word in text_lower for word in ['calculus', 'derivative', 'integral', 'limit']):
                subcategories.append("Calculus")
            if any(word in text_lower for word in ['algebra', 'equation', 'polynomial']):
                subcategories.append("Algebra")
            if any(word in text_lower for word in ['geometry', 'triangle', 'circle', 'angle']):
                subcategories.append("Geometry")
            if any(word in text_lower for word in ['statistics', 'probability', 'distribution']):
                subcategories.append("Statistics")
            if any(word in text_lower for word in ['matrix', 'vector', 'linear']):
                subcategories.append("Linear Algebra")
        
        elif domain == SubjectDomain.PHYSICS:
            if any(word in text_lower for word in ['mechanics', 'force', 'motion', 'velocity']):
                subcategories.append("Mechanics")
            if any(word in text_lower for word in ['quantum', 'wave', 'particle', 'schrodinger']):
                subcategories.append("Quantum Mechanics")
            if any(word in text_lower for word in ['electric', 'magnetic', 'field', 'current']):
                subcategories.append("Electromagnetism")
            if any(word in text_lower for word in ['thermodynamic', 'heat', 'temperature', 'entropy']):
                subcategories.append("Thermodynamics")
            if any(word in text_lower for word in ['relativity', 'einstein', 'space', 'time']):
                subcategories.append("Relativity")
        
        elif domain == SubjectDomain.CHEMISTRY:
            if any(word in text_lower for word in ['organic', 'carbon', 'bond']):
                subcategories.append("Organic Chemistry")
            if any(word in text_lower for word in ['reaction', 'equilibrium', 'rate']):
                subcategories.append("Chemical Kinetics")
            if any(word in text_lower for word in ['thermodynamic', 'enthalpy', 'entropy']):
                subcategories.append("Chemical Thermodynamics")
        
        return subcategories if subcategories else ["General"]


if __name__ == "__main__":
    # Test the classifier
    classifier = SubjectClassifier()
    
    # Test cases
    test_inputs = [
        "Calculate the derivative of x^2",
        "What is the capital of France?",
        "E = mc^2",
        "How do I bake a cake?",
        "Force equals mass times acceleration",
        "I need help with my taxes",
        "The Riemann zeta function",
        "What should I wear today?",
        "Solve the differential equation dy/dx = 2x",
        "Tell me about the history of Rome"
    ]
    
    print("Subject Matter Classification Tests")
    print("=" * 60)
    for input_text in test_inputs:
        result = classifier.classify(input_text)
        print(f"\nInput: {input_text}")
        print(f"Domain: {result.domain.value}")
        print(f"Confidence: {result.confidence:.2f}")
        print(f"Subcategories: {result.subcategories}")
        if result.warning_message:
            print(f"⚠️  WARNING: {result.warning_message}")
        if result.suggestions:
            print(f"Suggestions:")
            for suggestion in result.suggestions:
                print(f"  - {suggestion}")