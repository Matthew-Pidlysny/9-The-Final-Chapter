#!/usr/bin/env python3
"""
NCX Linguistic Analyzer
Advanced pattern detection and linguistic analysis for NCX Magazine
"""

import re
import logging
from typing import Dict, List, Any, Optional, Tuple, Set
from collections import Counter
from datetime import datetime, timezone
import math

class LinguisticAnalyzer:
    """Advanced linguistic analysis for detecting hidden patterns"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger("LinguisticAnalyzer")
        
        # Pattern databases
        self.discretion_patterns = self.load_discretion_patterns()
        self.altruistic_patterns = self.load_altruistic_patterns()
        self.sovereignty_patterns = self.load_sovereignty_patterns()
        self.deception_patterns = self.load_deception_patterns()
        
        # Organization tracking
        self.tracked_orgs = config.get("tracked_organizations", [])
        
        # Analysis metrics
        self.metrics = {
            "texts_analyzed": 0,
            "patterns_detected": 0,
            "high_confidence_detections": 0
        }
    
    def load_discretion_patterns(self) -> Dict[str, List[str]]:
        """Load patterns for detecting business discretions"""
        return {
            "hidden_meetings": [
                r"behind\s+closed\s+doors",
                r"private\s+meeting",
                r"confidential\s+discussion",
                r"off\s+the\s+record",
                r"undisclosed\s+location",
                r"unnamed\s+sources?",
                r"sources?\s+familiar\s+with",
                r"people\s+close\s+to",
                r"insiders?\s+say",
                r"according\s+to\s+sources?"
            ],
            "sudden_changes": [
                r"unexpected\s+announcement",
                r"surprise\s+decision",
                r"abrupt\s+change",
                r"without\s+explanation",
                r"no\s+prior\s+indication",
                r"caught\s+off\s+guard",
                r"sudden\s+shift",
                r"out\s+of\s+nowhere"
            ],
            "unverifiable_claims": [
                r"cannot\s+be\s+verified",
                r"unconfirmed\s+reports?",
                r"alleged",
                r"reportedly",
                r"purportedly",
                r"claims?\s+that\s+cannot",
                r"no\s+evidence\s+to\s+support",
                r"unsubstantiated"
            ],
            "power_moves": [
                r"strategic\s+acquisition",
                r"hostile\s+takeover",
                r"merger\s+talks",
                r"consolidation",
                r"market\s+dominance",
                r"monopoly",
                r"controlling\s+interest",
                r"board\s+shake-?up"
            ]
        }
    
    def load_altruistic_patterns(self) -> Dict[str, List[str]]:
        """Load patterns for detecting altruistic conspiracy indicators"""
        return {
            "sudden_philanthropy": [
                r"announces?\s+donation",
                r"charitable\s+foundation",
                r"giving\s+back",
                r"philanthrop(?:y|ic)",
                r"humanitarian\s+efforts?",
                r"social\s+responsibility",
                r"pledges?\s+to\s+donate",
                r"commits?\s+to\s+giving"
            ],
            "metaphysical_endorsement": [
                r"spiritual\s+awakening",
                r"consciousness",
                r"enlightenment",
                r"metaphysical",
                r"transcendent",
                r"higher\s+purpose",
                r"cosmic",
                r"universal\s+truth"
            ],
            "image_rehabilitation": [
                r"rebranding",
                r"new\s+direction",
                r"turning\s+over\s+a\s+new\s+leaf",
                r"fresh\s+start",
                r"reformed",
                r"changed\s+(?:man|woman|person)",
                r"redemption",
                r"making\s+amends"
            ],
            "timing_suspicion": [
                r"just\s+(?:days|weeks|months)\s+(?:after|before)",
                r"coincidentally",
                r"convenient\s+timing",
                r"shortly\s+(?:after|before)",
                r"in\s+the\s+wake\s+of",
                r"following\s+(?:allegations|scandal|controversy)"
            ]
        }
    
    def load_sovereignty_patterns(self) -> Dict[str, List[str]]:
        """Load patterns for detecting sovereignty and untouchability"""
        return {
            "legal_immunity": [
                r"above\s+the\s+law",
                r"immune\s+(?:from|to)",
                r"untouchable",
                r"protected\s+(?:by|from)",
                r"diplomatic\s+immunity",
                r"sovereign\s+immunity",
                r"beyond\s+(?:jurisdiction|reach)",
                r"cannot\s+be\s+prosecuted"
            ],
            "elite_status": [
                r"elite",
                r"establishment",
                r"inner\s+circle",
                r"privileged\s+(?:class|few)",
                r"power\s+brokers?",
                r"ruling\s+class",
                r"oligarch",
                r"plutocrat"
            ],
            "religious_authority": [
                r"divine\s+right",
                r"ordained",
                r"chosen",
                r"sacred\s+duty",
                r"higher\s+calling",
                r"spiritual\s+authority",
                r"religious\s+exemption",
                r"faith-based\s+immunity"
            ],
            "defiance_of_law": [
                r"refuses?\s+to\s+comply",
                r"ignores?\s+(?:court|law|order)",
                r"defies?\s+(?:authorities|law)",
                r"above\s+scrutiny",
                r"no\s+accountability",
                r"operates?\s+with\s+impunity",
                r"seemingly\s+untouchable"
            ]
        }
    
    def load_deception_patterns(self) -> Dict[str, List[str]]:
        """Load patterns for detecting potential deception"""
        return {
            "vague_language": [
                r"may\s+have",
                r"could\s+be",
                r"possibly",
                r"potentially",
                r"allegedly",
                r"reportedly",
                r"sources?\s+suggest",
                r"it\s+is\s+believed"
            ],
            "misdirection": [
                r"focus\s+on",
                r"pay\s+attention\s+to",
                r"what\s+really\s+matters",
                r"the\s+real\s+issue",
                r"distraction",
                r"smokescreen",
                r"red\s+herring"
            ],
            "contradiction": [
                r"despite\s+(?:earlier|previous)",
                r"contrary\s+to",
                r"in\s+contrast\s+to",
                r"however",
                r"but\s+(?:now|today)",
                r"changed\s+(?:position|stance)",
                r"reversal"
            ]
        }
    
    def analyze_text(self, text: str, source_url: str = "") -> Dict[str, Any]:
        """Comprehensive text analysis"""
        self.metrics["texts_analyzed"] += 1
        
        analysis = {
            "discretion_score": 0.0,
            "altruistic_score": 0.0,
            "sovereignty_score": 0.0,
            "deception_score": 0.0,
            "organization_mentions": [],
            "detected_patterns": [],
            "evidence_strength": 0.0,
            "punk_rating": 0,
            "should_publish": False,
            "reasoning": ""
        }
        
        # Analyze for each pattern type
        discretion_results = self.detect_discretion_patterns(text)
        altruistic_results = self.detect_altruistic_patterns(text)
        sovereignty_results = self.detect_sovereignty_patterns(text)
        deception_results = self.detect_deception_patterns(text)
        org_results = self.detect_organizations(text)
        
        # Calculate scores
        analysis["discretion_score"] = discretion_results["score"]
        analysis["altruistic_score"] = altruistic_results["score"]
        analysis["sovereignty_score"] = sovereignty_results["score"]
        analysis["deception_score"] = deception_results["score"]
        
        # Combine detected patterns
        analysis["detected_patterns"].extend(discretion_results["patterns"])
        analysis["detected_patterns"].extend(altruistic_results["patterns"])
        analysis["detected_patterns"].extend(sovereignty_results["patterns"])
        analysis["detected_patterns"].extend(deception_results["patterns"])
        
        # Organization mentions
        analysis["organization_mentions"] = org_results["organizations"]
        
        # Calculate overall evidence strength
        analysis["evidence_strength"] = self.calculate_evidence_strength(
            discretion_results["score"],
            altruistic_results["score"],
            sovereignty_results["score"],
            deception_results["score"],
            len(org_results["organizations"])
        )
        
        # Calculate punk rating (1-5 skulls)
        analysis["punk_rating"] = self.calculate_punk_rating(analysis)
        
        # Determine if should publish
        should_publish, reasoning = self.should_publish_analysis(analysis)
        analysis["should_publish"] = should_publish
        analysis["reasoning"] = reasoning
        
        if should_publish:
            self.metrics["high_confidence_detections"] += 1
        
        self.metrics["patterns_detected"] += len(analysis["detected_patterns"])
        
        return analysis
    
    def detect_discretion_patterns(self, text: str) -> Dict[str, Any]:
        """Detect business discretion patterns"""
        text_lower = text.lower()
        detected = []
        score = 0.0
        
        for category, patterns in self.discretion_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, text_lower, re.IGNORECASE)
                if matches:
                    detected.append(f"Discretion/{category}: {matches[0]}")
                    score += 0.1
        
        return {
            "score": min(1.0, score),
            "patterns": detected
        }
    
    def detect_altruistic_patterns(self, text: str) -> Dict[str, Any]:
        """Detect altruistic conspiracy patterns"""
        text_lower = text.lower()
        detected = []
        score = 0.0
        
        for category, patterns in self.altruistic_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, text_lower, re.IGNORECASE)
                if matches:
                    detected.append(f"Altruistic/{category}: {matches[0]}")
                    score += 0.15
        
        return {
            "score": min(1.0, score),
            "patterns": detected
        }
    
    def detect_sovereignty_patterns(self, text: str) -> Dict[str, Any]:
        """Detect sovereignty and untouchability patterns"""
        text_lower = text.lower()
        detected = []
        score = 0.0
        
        for category, patterns in self.sovereignty_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, text_lower, re.IGNORECASE)
                if matches:
                    detected.append(f"Sovereignty/{category}: {matches[0]}")
                    score += 0.2
        
        return {
            "score": min(1.0, score),
            "patterns": detected
        }
    
    def detect_deception_patterns(self, text: str) -> Dict[str, Any]:
        """Detect potential deception patterns"""
        text_lower = text.lower()
        detected = []
        score = 0.0
        
        for category, patterns in self.deception_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, text_lower, re.IGNORECASE)
                if matches:
                    detected.append(f"Deception/{category}: {matches[0]}")
                    score += 0.1
        
        return {
            "score": min(1.0, score),
            "patterns": detected
        }
    
    def detect_organizations(self, text: str) -> Dict[str, Any]:
        """Detect mentions of tracked organizations"""
        detected_orgs = []
        
        for org in self.tracked_orgs:
            # Case-insensitive search
            if re.search(re.escape(org), text, re.IGNORECASE):
                detected_orgs.append(org)
        
        return {
            "organizations": detected_orgs,
            "count": len(detected_orgs)
        }
    
    def calculate_evidence_strength(self, discretion: float, altruistic: float, 
                                   sovereignty: float, deception: float, 
                                   org_count: int) -> float:
        """Calculate overall evidence strength"""
        # Weighted combination
        base_score = (
            discretion * 0.25 +
            altruistic * 0.30 +
            sovereignty * 0.35 +
            deception * 0.10
        )
        
        # Boost for organization mentions
        org_boost = min(0.2, org_count * 0.05)
        
        total = min(1.0, base_score + org_boost)
        return round(total, 3)
    
    def calculate_punk_rating(self, analysis: Dict[str, Any]) -> int:
        """Calculate punk rating (1-5 skulls 💀)"""
        evidence = analysis["evidence_strength"]
        pattern_count = len(analysis["detected_patterns"])
        org_count = len(analysis["organization_mentions"])
        
        # Base rating on evidence strength
        if evidence >= 0.8 and pattern_count >= 5:
            return 5  # 💀💀💀💀💀
        elif evidence >= 0.7 and pattern_count >= 4:
            return 4  # 💀💀💀💀
        elif evidence >= 0.6 and pattern_count >= 3:
            return 3  # 💀💀💀
        elif evidence >= 0.5 and pattern_count >= 2:
            return 2  # 💀💀
        elif evidence >= 0.4:
            return 1  # 💀
        else:
            return 0  # Not punk enough
    
    def should_publish_analysis(self, analysis: Dict[str, Any]) -> Tuple[bool, str]:
        """Determine if analysis has enough value to publish"""
        evidence = analysis["evidence_strength"]
        punk_rating = analysis["punk_rating"]
        pattern_count = len(analysis["detected_patterns"])
        org_count = len(analysis["organization_mentions"])
        
        min_evidence = self.config.get("minimum_evidence_score", 0.6)
        min_punk = self.config.get("minimum_punk_rating", 3)
        
        # Must meet minimum thresholds
        if evidence < min_evidence:
            return False, f"Evidence too weak ({evidence:.2f} < {min_evidence})"
        
        if punk_rating < min_punk:
            return False, f"Not punk enough ({punk_rating} < {min_punk} skulls)"
        
        if pattern_count < 3:
            return False, f"Insufficient patterns detected ({pattern_count} < 3)"
        
        # Strong cases
        if evidence >= 0.8 and org_count >= 1:
            return True, f"Strong evidence ({evidence:.2f}) with org mentions"
        
        if evidence >= 0.7 and pattern_count >= 5:
            return True, f"High evidence ({evidence:.2f}) with multiple patterns"
        
        if punk_rating >= 4 and pattern_count >= 4:
            return True, f"High punk rating ({punk_rating} skulls) with solid patterns"
        
        # Borderline cases
        if evidence >= min_evidence and punk_rating >= min_punk and pattern_count >= 3:
            return True, f"Meets all minimum thresholds"
        
        return False, "Does not meet publication criteria"
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get analysis metrics"""
        return {
            **self.metrics,
            "detection_rate": self.metrics["high_confidence_detections"] / max(1, self.metrics["texts_analyzed"])
        }

def test_linguistic_analyzer():
    """Test the linguistic analyzer"""
    config = {
        "minimum_evidence_score": 0.6,
        "minimum_punk_rating": 3,
        "tracked_organizations": [
            "Lucis Trust",
            "Theosophical Society",
            "Freemasons"
        ]
    }
    
    analyzer = LinguisticAnalyzer(config)
    
    # Test text with multiple patterns
    test_text = """
    Behind closed doors, executives from major corporations met with unnamed sources 
    to discuss a surprise merger. The CEO, who has recently announced a major 
    philanthropic initiative focused on spiritual awakening and consciousness, 
    seems untouchable despite ongoing investigations. Sources familiar with the 
    matter say the Freemasons were involved in facilitating the deal, though 
    this cannot be verified. The timing is suspicious, coming just days after 
    allegations of financial misconduct.
    """
    
    print("🎸 Testing NCX Linguistic Analyzer...")
    print("=" * 60)
    
    results = analyzer.analyze_text(test_text)
    
    print(f"\n📊 Analysis Results:")
    print(f"   Evidence Strength: {results['evidence_strength']:.2f}")
    print(f"   Punk Rating: {'💀' * results['punk_rating']} ({results['punk_rating']}/5)")
    print(f"   Should Publish: {'✅ YES' if results['should_publish'] else '❌ NO'}")
    print(f"   Reasoning: {results['reasoning']}")
    
    print(f"\n🔍 Scores:")
    print(f"   Discretion: {results['discretion_score']:.2f}")
    print(f"   Altruistic: {results['altruistic_score']:.2f}")
    print(f"   Sovereignty: {results['sovereignty_score']:.2f}")
    print(f"   Deception: {results['deception_score']:.2f}")
    
    print(f"\n📋 Detected Patterns ({len(results['detected_patterns'])}):")
    for pattern in results['detected_patterns'][:5]:
        print(f"   • {pattern}")
    
    print(f"\n🏛️ Organizations Mentioned ({len(results['organization_mentions'])}):")
    for org in results['organization_mentions']:
        print(f"   • {org}")
    
    print(f"\n📈 Metrics:")
    metrics = analyzer.get_metrics()
    for key, value in metrics.items():
        print(f"   {key}: {value}")

if __name__ == "__main__":
    test_linguistic_analyzer()