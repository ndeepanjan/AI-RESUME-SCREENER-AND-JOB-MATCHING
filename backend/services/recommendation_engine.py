from typing import Dict, List, Optional


def generate_jd_recommendations(jd_comparison: Optional[Dict]) -> List[Dict]:
    """
    Generate a small set of actionable, evidence-based recommendations.

    This function only interprets the existing JD comparison.
    It does not modify or recalculate matching or scoring.
    """

    if not jd_comparison:
        return []

    recommendations = []

    matched_skills = jd_comparison.get("matched_skills", []) or []
    missing_skills = jd_comparison.get("missing_skills", []) or []
    matched_lower = {str(skill).lower() for skill in matched_skills}
    missing_lower = {str(skill).lower() for skill in missing_skills}

    def add_recommendation(title: str, suggestion: str, rec_type: str):
        recommendations.append({
            "icon": "💡",
            "title": title,
            "suggestion": suggestion,
            "type": rec_type,
        })

    # ---------------------------------------------------------
    # 1. ML / Data projects without clear evaluation evidence
    # ---------------------------------------------------------
    ml_skills = {
        "machine learning",
        "deep learning",
        "ml",
        "dl",
    }

    if matched_lower.intersection(ml_skills):
        add_recommendation(
            "Strengthen ML project evidence",
            "For your strongest ML project, mention the model used and an evaluation metric such as accuracy, F1-score, MAE, RMSE, or R² when available.",
            "project_evidence",
        )

    # ---------------------------------------------------------
    # 2. REST API recommendation
    # ---------------------------------------------------------
    if "rest apis" in missing_lower or "rest api" in missing_lower:
        add_recommendation(
            "Strengthen API experience",
            "If you have built or consumed an API, explicitly describe the REST API, endpoint, or backend functionality in your project or experience section.",
            "api",
        )

    # ---------------------------------------------------------
    # 3. Version control recommendation
    # ---------------------------------------------------------
    if "git" in missing_lower and "github" in matched_lower:
        add_recommendation(
            "Clarify version-control experience",
            "Your resume mentions GitHub but does not provide sufficient evidence for Git. If you genuinely used Git for version control, mention it explicitly.",
            "version_control",
        )

    # ---------------------------------------------------------
    # 4. Docker recommendation
    # ---------------------------------------------------------
    if "docker" in missing_lower:
        add_recommendation(
            "Consider adding containerization experience",
            "If Docker is relevant to your target role, gain hands-on experience through a genuine project and describe how you used it.",
            "docker",
        )

    # ---------------------------------------------------------
    # 5. Cloud recommendation
    # ---------------------------------------------------------
    cloud_skills = {"aws", "gcp", "azure", "cloud platforms"}

    missing_cloud = [
        skill for skill in cloud_skills
        if skill in missing_lower
    ]

    if missing_cloud:
        add_recommendation(
            "Consider relevant cloud experience",
            f"If cloud skills are important for the target role, gain genuine hands-on experience with {missing_cloud[0].upper()} through a project before listing it.",
            "cloud",
        )

    # ---------------------------------------------------------
    # 6. Data / ML tooling recommendation
    # ---------------------------------------------------------
    if "data visualization" in missing_lower:
        add_recommendation(
            "Strengthen data-visualization evidence",
            "If you have created charts or visual analysis in a project, explicitly mention the visualization tools and what insights you produced.",
            "data_visualization",
        )

    # ---------------------------------------------------------
    # 7. Feature engineering recommendation
    # ---------------------------------------------------------
    if "feature engineering" in missing_lower and (
        "machine learning" in matched_lower or
        "ml" in matched_lower
    ):
        add_recommendation(
            "Document feature-engineering work",
            "If you performed feature selection, transformation, encoding, scaling, or other feature-engineering steps, describe them in the relevant ML project.",
            "feature_engineering",
        )

    # ---------------------------------------------------------
    # Remove duplicates and keep recommendations concise
    # ---------------------------------------------------------
    unique = []
    seen = set()

    for rec in recommendations:
        key = rec["suggestion"].strip().lower()

        if key not in seen:
            seen.add(key)
            unique.append(rec)

    # Keep the dashboard concise.
    return unique[:5]
