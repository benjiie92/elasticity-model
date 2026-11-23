
import streamlit as st
from io import BytesIO
import pandas as pd
import numpy as np
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Pricing Intelligence System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM DASHBOARD THEME
# --------------------------------------------------

st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #F4F7FB;
    color: black;
}

/* Improve Markdown text visibility */
[data-testid="stMarkdownContainer"] {
    color: #1F2937;
}

/* Preserve individual text styling */
[data-testid="stMarkdownContainer"] p {
    opacity: 1;
    visibility: visible;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #101C35 0%, #172B4D 100%);
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Main headings */
h1 {
    color: white !important;
    font-weight: 750 !important;
    letter-spacing: -0.8px;
}

h2, h3 {
    color: #1E3A5F !important;
    font-weight: 650 !important;
}

/* KPI metric cards */
[data-testid="stMetric"] {
    background: #FFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E5EAF2;
    box-shadow: 0 3px 12px rgba(20, 43, 78, 0.05);
}

/* Metric labels */
[data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-weight: 600;
}

/* Metric values */
[data-testid="stMetricValue"] {
    color: #1457A6 !important;
    font-weight: 750;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    background: #1769AA;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.55rem 1.2rem;
    font-weight: 600;
    transition: 0.2s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #0E4F85;
    color: white;
    border: none;
}

/* Dataframes and tables */
[data-testid="stDataFrame"] {
    border: 1px solid #E5EAF2;
    border-radius: 10px;
    overflow: hidden;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-weight: 600;
    color: #64748B;
}

.stTabs [aria-selected="true"] {
    color: blue !important;
}

/* Input fields */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 8px;
}

.st-key-product_department_filter label,
.st-key-product_department_filter [data-baseweb="select"],
.st-key-product_department_filter [data-baseweb="select"] * {
    color: #000000 !important;
}

/* Information messages */
[data-testid="stAlertContainer"] {
    background-color: #D6EAF8 !important;
    border-radius: 10px !important;
    padding: 15px !important;
}

/* Sidebar information message */
[data-testid="stSidebar"] [data-testid="stAlertContainer"] {
    background-color: #ffffff !important;
    border-radius: 10px !important;
    padding: 12px !important;
}

[data-testid="stSidebar"] [data-testid="stAlertContainer"] p {
    color: #1E3A5F !important;
}

/* Dividers */
hr {
    border-color: #E2E8F0;
}

/* Sidebar navigation spacing */
[data-testid="stSidebarNav"] {
    padding-top: 1rem;
}

/* Diagnostic fix: force visible text in Streamlit Markdown */
/* Ensure Markdown paragraph text remains visible */
[data-testid="stMarkdownContainer"] p {
    opacity: 1 !important;
    visibility: visible !important;
}



</style>
""", unsafe_allow_html=True)

DATA_DIR = Path(__file__).parent / "pricing_dashboard_data"


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data(filename):
    return pd.read_csv(DATA_DIR / filename)


management = load_data("management_dashboard.csv")
products = load_data("integrated_product_opportunities.csv")
segments = load_data("department_income_elasticity.csv")
customer_demographics = load_data("customer_demographics.csv")
profitability = load_data("profitability_portfolio.csv")
increase_scenarios = load_data("all_product_simulations.csv")
reduction_scenarios = load_data("price_reduction_results.csv")


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
# --------------------------------------------------
# PRICEIQ SIDEBAR
# --------------------------------------------------

st.sidebar.markdown("""
<div style="padding: 15px 5px 20px 5px;">
    <h1 style="color: white !important;
               font-size: 30px;
               font-weight: 800;
               margin-bottom: 0;">
        PRICE<span style="color: #38BDF8;">IQ</span>
    </h1>
    <p style="color: #94A3B8;
              font-size: 11px;
              letter-spacing: 1.5px;
              margin-top: 5px;">
        PRICING INTELLIGENCE PLATFORM
    </p>

    
</div>
""", unsafe_allow_html=True)

st.sidebar.divider()

st.sidebar.caption("NAVIGATION")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Overview",
        "Product Intelligence",
        "Customer Segments",
        "Pricing Simulator",
        "Profitability Analysis",
        "Custom Elasticity Estimator"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()

st.sidebar.info(
    "Analytical pricing recommendations. "
    "All proposed price changes require business review and approval."
)

st.sidebar.markdown("""
<div style="position: fixed;
            bottom: 20px;
            color: #94A3B8;
            font-size: 11px;">
    PRICEIQ • PRICING ANALYTICS
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# EXECUTIVE OVERVIEW
# --------------------------------------------------


if page == "Executive Overview":

    # --------------------------------------------------
    # EXECUTIVE HEADER
    # --------------------------------------------------

    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #102544, #1769AA);
        padding: 30px;
        border-radius: 16px;
        margin-bottom: 25px;
    ">
        <p style="color:#7DD3FC; font-size:12px;
                  letter-spacing:2px; font-weight:700;">
            PRICING INTELLIGENCE PLATFORM
        </p>
        <h1 style="color:white !important;
                   font-size:34px; margin-bottom:8px;">
            Executive Overview
        </h1>
        <p style="color:#DBEAFE; font-size:15px; margin-bottom:0;">
            Monitor pricing opportunities, product performance
            and revenue scenarios across your retail portfolio.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------
    # KEY BUSINESS METRICS
    # --------------------------------------------------

    total_products = len(management)

    potential_revenue = management["additional_revenue_5pct"].sum()

    avg_elasticity = management["elasticity"].mean()

    five_pct = (
        management["recommended_test_increase_pct"] == 5
    ).sum()

    three_pct = (
        management["recommended_test_increase_pct"] == 3
    ).sum()

    segment_coverage = (
        management["evidence_coverage"].notna().sum()
    )

    cost_pending = total_products

    st.markdown("### Portfolio Performance")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Products Analysed",
        f"{total_products:,}",
        help="Number of products included in the pricing opportunity portfolio."
    )

    c2.metric(
        "Potential Revenue",
        f"{potential_revenue:,.2f}",
        help="Modelled additional revenue under the 5% price increase scenario. Not profit or guaranteed revenue."
    )

    c3.metric(
        "Average Price Elasticity",
        f"{avg_elasticity:.3f}",
        help="Average estimated price elasticity across the analysed products."
    )

    st.markdown("### Pricing Strategy Indicators")

    c4, c5, c6 = st.columns(3)

    c4.metric("Proposed 5% Tests", int(five_pct))
    c5.metric("Proposed 3% Tests", int(three_pct))
    c6.metric("Awaiting Cost Data", int(cost_pending))

    # --------------------------------------------------
    # OPPORTUNITY TABLE
    # --------------------------------------------------

    st.divider()

    st.markdown("### 🎯 Top Pricing Opportunities")

    st.caption(
        "Products ranked by modelled additional revenue "
        "under the 5% price increase scenario."
    )

    display_columns = [
        "PRODUCT_ID",
        "COMMODITY_DESC",
        "DEPARTMENT",
        "elasticity",
        "additional_revenue_5pct",
        "recommended_test_increase_pct",
        "business_review_status"
    ]

    available_columns = [
        c for c in display_columns if c in management.columns
    ]

    st.dataframe(
        management[available_columns].sort_values(
            "additional_revenue_5pct",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )

        # --------------------------------------------------
    # PRICING OPPORTUNITY VISUALIZATION
    # --------------------------------------------------

    st.divider()

    st.markdown("### 📈 Highest Revenue Opportunities")

    chart_data = (
        management.nlargest(10, "additional_revenue_5pct")
        .copy()
    )

    chart_data["Product"] = (
        chart_data["COMMODITY_DESC"].astype(str)
        + " ("
        + chart_data["PRODUCT_ID"].astype(str)
        + ")"
    )

    chart_data = chart_data.sort_values(
        "additional_revenue_5pct",
        ascending=True
    )

    st.bar_chart(
        chart_data.set_index("Product")["additional_revenue_5pct"],
        horizontal=True
    )

    st.caption(
        "Modelled additional revenue under a 5% price increase scenario. "
        "These estimates are not guaranteed outcomes."
    )

    # --------------------------------------------------
    # BUSINESS EVIDENCE
    # --------------------------------------------------

    st.divider()

    st.markdown("### 📊 Analytical Coverage")

    coverage1, coverage2 = st.columns(2)

    coverage1.metric(
        "Products with Segment Evidence",
        int(segment_coverage)
    )

    coverage2.metric(
        "Products Awaiting Cost Information",
        int(cost_pending)
    )

    # --------------------------------------------------
    # MANAGEMENT CONSIDERATIONS
    # --------------------------------------------------

    st.markdown("### ⚠️ Important Business Considerations")

    st.warning(
        "Revenue figures are model-based scenarios, not guaranteed "
        "results. They are not profit estimates. Actual costs, competitor "
        "reactions, inventory and customer behaviour must be considered "
        "before approving a price change."
    )

    st.info(
        "Pricing recommendations are intended to support controlled "
        "business testing and management decisions. They should not "
        "be treated as automatic price-change instructions."
    )


# --------------------------------------------------
# PRODUCT INTELLIGENCE
# --------------------------------------------------
elif page == "Product Intelligence":

    # --------------------------------------------------
    # PRODUCT INTELLIGENCE HEADER
    # --------------------------------------------------

    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #102544, #1769AA);
        padding: 28px;
        border-radius: 16px;
        margin-bottom: 25px;
    ">
        <p style="color:#7DD3FC; font-size:12px;
                  letter-spacing:2px; font-weight:700;">
            PRODUCT ANALYTICS
        </p>
        <h1 style="color:white !important;
                   font-size:32px; margin-bottom:8px;">
            Product Intelligence
        </h1>
        <p style="color:#DBEAFE; font-size:14px; margin-bottom:0;">
            Understand product-level price sensitivity and identify
            commercial pricing opportunities.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------
    # DEPARTMENT FILTER
    # --------------------------------------------------

    departments = sorted(
        products["DEPARTMENT"].dropna().unique()
    )

    selected_department = st.selectbox(
        "Filter by department",
        ["All Departments"] + departments,
        key="product_department_filter"
    )

    filtered = products.copy()

    if selected_department != "All Departments":
        filtered = filtered[
            filtered["DEPARTMENT"] == selected_department
        ]

    # --------------------------------------------------
    # PRODUCT KPI METRICS
    # --------------------------------------------------

    total_products = len(filtered)

    avg_elasticity = filtered["elasticity"].mean()

    significant_products = (
        (filtered["adjusted_p_value"] < 0.05)
        & (filtered["upper_ci"] < 0)
    ).sum()

    potential_revenue = filtered[
        "additional_revenue_5pct"
    ].sum()

    st.markdown("### Product Performance")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Products Analysed",
        f"{total_products:,}"
    )

    c2.metric(
        "Average Elasticity",
        f"{avg_elasticity:.3f}"
    )

    c3.metric(
        "Statistically Significant",
        f"{significant_products:,}"
    )

    c4.metric(
        "Potential Revenue",
        f"{potential_revenue:,.2f}"
    )

    st.divider()

    # --------------------------------------------------
    # PRODUCT OPPORTUNITY CHART
    # --------------------------------------------------

    st.markdown("### 📈 Leading Product Opportunities")

    st.caption(
        "Top products ranked by modelled additional revenue "
        "under a 5% price increase scenario."
    )

    chart_data = filtered.nlargest(
        10,
        "additional_revenue_5pct"
    ).copy()

    if not chart_data.empty:

        chart_data["Product"] = (
            chart_data["COMMODITY_DESC"].astype(str)
            + " ("
            + chart_data["PRODUCT_ID"].astype(str)
            + ")"
        )

        chart_data = chart_data.sort_values(
            "additional_revenue_5pct",
            ascending=True
        )

        st.bar_chart(
            chart_data.set_index("Product")[
                "additional_revenue_5pct"
            ],
            horizontal=True
        )

    else:
        st.info("No product opportunities available for this department.")

    st.divider()

    # --------------------------------------------------
    # ELASTICITY COMPARISON
    # --------------------------------------------------

    st.markdown("### 📊 Price Elasticity Comparison")

    elasticity_chart = filtered.nlargest(
        15,
        "additional_revenue_5pct"
    ).copy()

    if not elasticity_chart.empty:

        elasticity_chart["Product"] = (
            elasticity_chart["COMMODITY_DESC"].astype(str)
            + " ("
            + elasticity_chart["PRODUCT_ID"].astype(str)
            + ")"
        )

        elasticity_chart = elasticity_chart.sort_values(
            "elasticity",
            ascending=True
        )

        st.bar_chart(
            elasticity_chart.set_index("Product")["elasticity"],
            horizontal=True
        )

    st.caption(
        "More negative elasticity indicates greater estimated "
        "demand sensitivity to price."
    )

    st.divider()

    # --------------------------------------------------
    # DETAILED PRODUCT RESULTS
    # --------------------------------------------------

    st.markdown("### 📋 Detailed Product Intelligence")

    product_columns = [
        "PRODUCT_ID",
        "COMMODITY_DESC",
        "DEPARTMENT",
        "elasticity",
        "lower_ci",
        "upper_ci",
        "adjusted_p_value",
        "baseline_sales",
        "baseline_quantity",
        "additional_revenue_5pct"
    ]

    available = [
        c for c in product_columns if c in filtered.columns
    ]

    st.dataframe(
        filtered[available].sort_values(
            "additional_revenue_5pct",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # ANALYTICAL INTERPRETATION
    # --------------------------------------------------

    st.markdown("### 💡 Analytical Interpretation")

    st.info(
        "Statistically significant negative elasticity estimates "
        "provide evidence of price-sensitive demand. Confidence "
        "intervals and adjusted p-values should be reviewed before "
        "considering pricing experiments."
    )

    st.warning(
        "These estimates are observational and should not be "
        "interpreted as guaranteed causal effects. Pricing decisions "
        "should consider promotions, competition, inventory and "
        "customer behaviour."
    )

# --------------------------------------------------
# CUSTOMER SEGMENTS
# --------------------------------------------------

elif page == "Customer Segments":

    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #102544, #1769AA);
        padding: 28px;
        border-radius: 16px;
        margin-bottom: 25px;
    ">
        <p style="color:#7DD3FC; font-size:12px;
                  letter-spacing:2px; font-weight:700;">
            CUSTOMER ANALYTICS
        </p>
        <h1 style="color:white !important;
                   font-size:32px; margin-bottom:8px;">
            Customer Segment Intelligence
        </h1>
        <p style="color:#DBEAFE; font-size:14px; margin-bottom:0;">
            Explore customer demographics, purchasing behaviour
            and department-level price sensitivity.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------
    # DATA VALIDATION
    # --------------------------------------------------

    demo = customer_demographics.copy()

    # --------------------------------------------------
    # THREE MAIN TABS
    # --------------------------------------------------

    tab1, tab2, tab3 = st.tabs([
        "Price Sensitivity",
        "Demographic Profile",
        "Purchasing Behaviour"
    ])

    # ==================================================
    # TAB 1: PRICE SENSITIVITY
    # ==================================================

    with tab1:

        st.subheader("Department-Level Price Sensitivity")

        department_options = sorted(
            segments["DEPARTMENT"].dropna().unique()
        )

        if department_options:

            selected_department = st.selectbox(
                "Select Department",
                department_options,
                key="segment_department"
            )

            segment_view = segments[
                segments["DEPARTMENT"] == selected_department
            ].copy()

            income_groups = segment_view["INCOME_DESC"].nunique()

            average_elasticity = segment_view["elasticity"].mean()

            reliable_negative = len(
                segment_view[
                    (segment_view["adjusted_p_value"] < 0.05)
                    & (segment_view["upper_ci"] < 0)
                ]
            )

            col1, col2, col3 = st.columns(3)

            col1.metric("Income Groups", income_groups)

            col2.metric(
                "Average Elasticity",
                f"{average_elasticity:.3f}"
            )

            col3.metric(
                "Reliable Negative Estimates",
                reliable_negative
            )

            st.divider()

            st.subheader("Income Group Elasticity")

            chart_data = (
                segment_view[
                    ["INCOME_DESC", "elasticity"]
                ]
                .dropna()
                .sort_values("elasticity")
                .set_index("INCOME_DESC")
            )

            st.bar_chart(chart_data, horizontal=True)

            st.subheader("Detailed Segment Estimates")

            st.dataframe(
                segment_view.sort_values(
                    "elasticity",
                    ascending=True
                ),
                use_container_width=True,
                hide_index=True
            )

            st.warning(
                "These are observational department-level estimates, "
                "not causal effects or product-specific household estimates."
            )

        else:
            st.warning("No department-level estimates available.")

    # ==================================================
    # TAB 2: DEMOGRAPHIC PROFILE
    # ==================================================

    with tab2:

        st.subheader("Customer Demographic Profile")

        total_households = demo["household_key"].nunique()

        demographic_households = demo[
            demo["AGE_DESC"].notna()
        ]["household_key"].nunique()

        coverage = (
            demographic_households / total_households * 100
            if total_households > 0 else 0
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Households Analysed",
            f"{total_households:,}"
        )

        col2.metric(
            "Households With Demographics",
            f"{demographic_households:,}"
        )

        col3.metric(
            "Demographic Coverage",
            f"{coverage:.1f}%"
        )

        st.divider()

        demographic_columns = {
            "Age Group": "AGE_DESC",
            "Income Group": "INCOME_DESC",
            "Marital Status": "MARITAL_STATUS_CODE",
            "Homeownership": "HOMEOWNER_DESC",
            "Household Composition": "HH_COMP_DESC",
            "Household Size": "HOUSEHOLD_SIZE_DESC",
            "Children": "KID_CATEGORY_DESC"
        }

        selected_demographic = st.selectbox(
            "Explore Demographic Category",
            list(demographic_columns.keys())
        )

        selected_column = demographic_columns[
            selected_demographic
        ]

        distribution = (
            demo[selected_column]
            .fillna("Unknown")
            .value_counts()
            .reset_index()
        )

        distribution.columns = [
            "Category",
            "Households"
        ]

        distribution["Percentage"] = (
            distribution["Households"]
            / distribution["Households"].sum() * 100
        )

        col1, col2 = st.columns([2, 1])

        with col1:

            st.markdown(
                f"#### Household Distribution: {selected_demographic}"
            )

            st.bar_chart(
                distribution.set_index("Category")["Households"],
                horizontal=True
            )

        with col2:

            st.markdown("#### Distribution Details")

            st.dataframe(
                distribution.style.format({
                    "Percentage": "{:.1f}%"
                }),
                use_container_width=True,
                hide_index=True
            )

        st.info(
            "Demographic information is available for only a subset "
            "of households. Missing and unknown categories are retained "
            "where possible."
        )

    # ==================================================
    # TAB 3: PURCHASING BEHAVIOUR
    # ==================================================

    with tab3:

        st.subheader("Demographic Purchasing Behaviour")

        behaviour_columns = {
            "Age Group": "AGE_DESC",
            "Income Group": "INCOME_DESC",
            "Household Composition": "HH_COMP_DESC",
            "Household Size": "HOUSEHOLD_SIZE_DESC",
            "Children": "KID_CATEGORY_DESC",
            "Homeownership": "HOMEOWNER_DESC"
        }

        selected_behaviour = st.selectbox(
            "Compare Purchasing Behaviour By",
            list(behaviour_columns.keys())
        )

        group_column = behaviour_columns[
            selected_behaviour
        ]

        behaviour_data = demo.dropna(
            subset=[group_column]
        ).copy()

        behaviour_summary = (
            behaviour_data
            .groupby(group_column)
            .agg(
                households=("household_key", "nunique"),
                average_spending=("total_spending", "mean"),
                median_spending=("total_spending", "median"),
                average_basket=("average_basket_spending", "mean"),
                average_trips=("shopping_trips", "mean"),
                average_quantity=("total_quantity", "mean")
            )
            .reset_index()
        )

        behaviour_summary = behaviour_summary.rename(
            columns={
                group_column: "Customer Group"
            }
        )

        st.markdown("### Household Spending")

        st.bar_chart(
            behaviour_summary.set_index("Customer Group")[
                "average_spending"
            ],
            horizontal=True
        )

        st.markdown("### Average Basket Spending")

        st.bar_chart(
            behaviour_summary.set_index("Customer Group")[
                "average_basket"
            ],
            horizontal=True
        )

        st.markdown("### Shopping Frequency")

        st.bar_chart(
            behaviour_summary.set_index("Customer Group")[
                "average_trips"
            ],
            horizontal=True
        )

        st.markdown("### Detailed Purchasing Behaviour")

        st.dataframe(
            behaviour_summary.style.format({
                "average_spending": "{:,.2f}",
                "median_spending": "{:,.2f}",
                "average_basket": "{:,.2f}",
                "average_trips": "{:,.2f}",
                "average_quantity": "{:,.2f}"
            }),
            use_container_width=True,
            hide_index=True
        )

        st.warning(
            "These comparisons describe observed purchasing behaviour. "
            "They do not establish that demographic characteristics "
            "cause differences in spending."
        )
# --------------------------------------------------
# PRICING SIMULATOR
# --------------------------------------------------

elif page == "Pricing Simulator":

    # --------------------------------------------------
    # PRICING SIMULATOR HEADER
    # --------------------------------------------------

    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #142B4E, #1769AA);
        padding: 28px;
        border-radius: 14px;
        margin-bottom: 25px;
    ">
        <p style="
            color: #BAE6FD;
            font-size: 12px;
            letter-spacing: 2px;
            margin-bottom: 8px;
        ">
            SCENARIO PLANNING
        </p>
        <h1 style="
            color: white !important;
            font-size: 30px;
            margin: 0;
        ">
            Pricing Simulator
        </h1>
        <p style="
            color: #E0F2FE;
            margin-top: 10px;
            margin-bottom: 0;
        ">
            Model how alternative price changes could affect product
            demand and revenue.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.caption(
        "Explore estimated revenue outcomes using historical product "
        "sales and estimated price elasticity."
    )

    # --------------------------------------------------
    # PRODUCT SELECTION
    # --------------------------------------------------

    st.markdown("### Select Product")

    product_options = products[
        ["PRODUCT_ID", "COMMODITY_DESC"]
    ].drop_duplicates()

    product_options["label"] = (
        product_options["COMMODITY_DESC"].astype(str)
        + " | ID: "
        + product_options["PRODUCT_ID"].astype(str)
    )

    selected_label = st.selectbox(
        "Choose a product to simulate",
        product_options["label"].tolist()
    )

    selected_id = product_options.loc[
        product_options["label"] == selected_label,
        "PRODUCT_ID"
    ].iloc[0]

    product = products[
        products["PRODUCT_ID"] == selected_id
    ].iloc[0]

    elasticity = float(product["elasticity"])
    baseline_sales = float(product["baseline_sales"])
    baseline_quantity = float(product["baseline_quantity"])

    current_price = baseline_sales / baseline_quantity

    st.divider()

    # --------------------------------------------------
    # BASELINE METRICS
    # --------------------------------------------------

    st.markdown("### Historical Product Baseline")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Average Price",
        f"{current_price:.2f}"
    )

    c2.metric(
        "Baseline Quantity",
        f"{baseline_quantity:,.0f}"
    )

    c3.metric(
        "Price Elasticity",
        f"{elasticity:.3f}"
    )

    # --------------------------------------------------
    # PRICE ADJUSTMENT
    # --------------------------------------------------

    st.divider()

    st.markdown("### Adjust Proposed Price")

    price_change = st.slider(
        "Proposed price change (%)",
        min_value=-20,
        max_value=20,
        value=5,
        step=1
    )

    change = price_change / 100

    new_price = current_price * (1 + change)

    quantity_change = (1 + change) ** elasticity - 1

    expected_quantity = baseline_quantity * (1 + quantity_change)

    projected_revenue = new_price * expected_quantity

    revenue_change = projected_revenue - baseline_sales

    revenue_change_pct = (
        revenue_change / baseline_sales
    ) * 100

    st.markdown(
        f"""
        <div style="
            background: white;
            border: 1px solid #E5EAF2;
            border-left: 5px solid #1769AA;
            padding: 18px;
            border-radius: 10px;
            margin-top: 10px;
        ">
            <p style="color: #64748B; margin: 0;">
                Proposed price adjustment
            </p>
            <h2 style="color: #1769AA; margin: 5px 0;">
                {price_change:+d}%
            </h2>
            <p style="color: #64748B; margin: 0;">
                New estimated average price: {new_price:.2f}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # SIMULATION RESULTS
    # --------------------------------------------------

    st.divider()

    st.markdown("### Simulation Results")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "New Average Price",
        f"{new_price:.2f}",
        f"{price_change:+d}%"
    )

    c2.metric(
        "Expected Quantity",
        f"{expected_quantity:,.2f}",
        f"{quantity_change * 100:+.2f}%"
    )

    c3.metric(
        "Projected Revenue",
        f"{projected_revenue:,.2f}",
        f"{revenue_change_pct:+.2f}%"
    )

    st.metric(
        "Estimated Revenue Change",
        f"{revenue_change:+,.2f}",
        f"{revenue_change_pct:+.2f}%"
    )

    # --------------------------------------------------
    # SCENARIO COMPARISON
    # --------------------------------------------------

    st.divider()

    st.markdown("### Alternative Pricing Scenarios")

    scenario_changes = [-20, -15, -10, -5, 0, 5, 10, 15, 20]

    scenario_data = []

    for scenario in scenario_changes:

        scenario_rate = scenario / 100

        scenario_price = current_price * (1 + scenario_rate)

        scenario_quantity = (
            baseline_quantity
            * (1 + scenario_rate) ** elasticity
        )

        scenario_revenue = (
            scenario_price * scenario_quantity
        )

        scenario_data.append({
            "Price Change (%)": scenario,
            "Estimated Price": scenario_price,
            "Expected Quantity": scenario_quantity,
            "Projected Revenue": scenario_revenue,
            "Revenue Change": scenario_revenue - baseline_sales
        })

    scenario_df = pd.DataFrame(scenario_data)

    chart_data = scenario_df[
        ["Price Change (%)", "Projected Revenue"]
    ].set_index("Price Change (%)")

    st.line_chart(chart_data)

    st.dataframe(
        scenario_df.style.format({
            "Estimated Price": "{:.2f}",
            "Expected Quantity": "{:,.2f}",
            "Projected Revenue": "{:,.2f}",
            "Revenue Change": "{:+,.2f}"
        }),
        use_container_width=True
    )

    # --------------------------------------------------
    # BUSINESS INTERPRETATION
    # --------------------------------------------------

    st.divider()

    st.markdown("### Business Interpretation")

    if revenue_change > 0:

        st.success(
            f"The proposed price change produces a modelled revenue "
            f"increase of {revenue_change:+,.2f}. "
            "This scenario may be worth further commercial evaluation."
        )

    elif revenue_change < 0:

        st.warning(
            f"The proposed price change produces a modelled revenue "
            f"decrease of {revenue_change:,.2f}. "
            "Review the demand response before considering this change."
        )

    else:

        st.info(
            "The proposed scenario produces no estimated revenue change."
        )

    st.warning(
        "This simulation assumes constant price elasticity. It does not "
        "account for costs, competitors, stock availability, customer "
        "switching or changing market conditions. These are modelled "
        "revenue scenarios, not guaranteed outcomes or profit forecasts."
    )

# --------------------------------------------------
# PROFITABILITY ANALYSIS
# --------------------------------------------------

elif page == "Profitability Analysis":

    # --------------------------------------------------
    # PROFITABILITY HEADER
    # --------------------------------------------------

    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #142B4E, #1769AA);
        padding: 28px;
        border-radius: 14px;
        margin-bottom: 25px;
    ">
        <p style="
            color: #BAE6FD;
            font-size: 12px;
            letter-spacing: 2px;
            margin-bottom: 8px;
        ">
            FINANCIAL PERFORMANCE
        </p>
        <h1 style="
            color: white !important;
            font-size: 30px;
            margin: 0;
        ">
            Profitability Analysis
        </h1>
        <p style="
            color: #E0F2FE;
            margin-top: 10px;
            margin-bottom: 0;
        ">
            Evaluate product costs, gross margins and potential
            profitability opportunities.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.caption(
        "Gross-profit evaluation requires actual retailer unit costs "
        "and current selling prices."
    )

    # --------------------------------------------------
    # COST DATA STATUS
    # --------------------------------------------------

    st.markdown("### Product Cost Data Status")

    cost_columns = [
        "current_unit_cost",
        "current_unit_price"
    ]

    available_cost_columns = [
        c for c in cost_columns if c in profitability.columns
    ]

    if available_cost_columns:

        complete_cost_data = profitability[
            available_cost_columns
        ].notna().all(axis=1)

        ready = int(complete_cost_data.sum())
        pending = len(profitability) - ready

    else:

        ready = 0
        pending = len(profitability)

    total_products = len(profitability)

    coverage = (
        (ready / total_products) * 100
        if total_products > 0
        else 0
    )

    # --------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Products Analysed",
        f"{total_products:,}"
    )

    c2.metric(
        "Cost Data Available",
        f"{ready:,}"
    )

    c3.metric(
        "Awaiting Cost Data",
        f"{pending:,}"
    )

    c4.metric(
        "Cost Data Coverage",
        f"{coverage:.1f}%"
    )

    st.divider()

    # --------------------------------------------------
    # COST DATA COVERAGE
    # --------------------------------------------------

    st.markdown("### Financial Data Readiness")

    if total_products > 0:

        coverage_data = pd.DataFrame({
            "Status": [
                "Cost data available",
                "Awaiting cost data"
            ],
            "Products": [
                ready,
                pending
            ]
        })

        st.bar_chart(
            coverage_data.set_index("Status"),
            horizontal=True
        )

    # --------------------------------------------------
    # PRODUCT COST INFORMATION
    # --------------------------------------------------

    st.divider()

    st.markdown("### Product Cost Information")

    st.dataframe(
        profitability,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # PROFITABILITY READINESS
    # --------------------------------------------------

    st.divider()

    st.markdown("### Gross Profit Analysis")

    if ready == 0:

        st.warning(
            "Profitability analysis is currently awaiting actual "
            "product cost and selling price information."
        )

        st.info(
            "The system can estimate revenue changes using price "
            "elasticity, but it cannot establish whether those changes "
            "will improve gross profit without actual unit costs."
        )

        st.markdown("#### Required Financial Information")

        required_fields = pd.DataFrame({
            "Required Field": [
                "PRODUCT_ID",
                "current_unit_cost",
                "current_unit_price"
            ],
            "Purpose": [
                "Identify the product",
                "Calculate product cost",
                "Calculate selling revenue and gross margin"
            ]
        })

        st.dataframe(
            required_fields,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.success(
            f"{ready} products have the required cost and price fields."
        )

        st.info(
            "Review the supplied financial data before interpreting "
            "gross-profit results. Confirm that all costs and prices "
            "are valid and comparable."
        )

    # --------------------------------------------------
    # BUSINESS RECOMMENDATIONS
    # --------------------------------------------------

    st.divider()

    st.markdown("### Business Recommendations")

    st.markdown("""
    **1. Collect actual product costs**

    Obtain unit acquisition costs or cost of goods sold from the retailer.

    **2. Confirm current selling prices**

    Ensure the supplied prices reflect current commercial conditions.

    **3. Evaluate gross margins**

    Calculate gross profit and gross margin for each product once
    the financial inputs are available.

    **4. Combine elasticity and profitability**

    Identify products where demand sensitivity and gross-margin
    performance support commercially viable pricing decisions.
    """)

    st.warning(
        "Revenue growth does not automatically mean profit growth. "
        "All pricing decisions should consider product costs, margins, "
        "competitor activity and customer response."
    )



# --------------------------------------------------
# CUSTOM ELASTICITY ESTIMATOR
# --------------------------------------------------

elif page == "Custom Elasticity Estimator":

    # --------------------------------------------------
# CUSTOM ELASTICITY ESTIMATOR HEADER
# --------------------------------------------------

    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #142B4E, #1769AA);
        padding: 28px;
        border-radius: 14px;
        margin-bottom: 25px;
    ">
        <p style="
            color: #BAE6FD;
            font-size: 12px;
            letter-spacing: 2px;
            margin-bottom: 8px;
        ">
            ADVANCED PRICING ANALYTICS
        </p>
        <h1 style="
            color: white !important;
            font-size: 30px;
            margin: 0;
        ">
            Custom Elasticity Estimator
        </h1>
        <p style="
            color: #E0F2FE;
            margin-top: 10px;
            margin-bottom: 0;
        ">
            Estimate price sensitivity using your own historical
            selling prices and quantities.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Create an estimate using manual observations or import "
        "your historical sales data from a CSV or Excel file."
    )

    tab1, tab2 = st.tabs([
        "Manual Entry",
        "Import Historical Data"
        ])

    with tab1:

        st.markdown("### 📝 Enter Historical Observations")

        st.caption(
            "Add one observation per period, such as weekly or monthly sales."
        )

        st.info(
            "Required information: selling price and quantity sold. "
            "Promotion data is optional."
    )

        default_data = pd.DataFrame({
            "Period": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"],
            "Selling Price": [10.00, 10.50, 9.50, 11.00, 10.00],
            "Quantity Sold": [500, 470, 530, 445, 510],
            "Promotion": [False, False, True, False, False]
        })

        manual_data = st.data_editor(
            default_data,
            num_rows="dynamic",
            use_container_width=True,
            key="manual_elasticity_data"
        )

        manual_data = manual_data.copy()

        st.session_state["custom_elasticity_data"] = manual_data

        st.caption(
            "The example figures are illustrative. Replace them "
            "with your actual historical observations."
        )

    with tab2:

        st.markdown("### 📂 Import Historical Sales Data")

        st.caption(
            "Upload your historical sales records to estimate "
            "price elasticity automatically."
        )
        uploaded_file = st.file_uploader(
            "Upload historical sales data",
            type=["csv", "xlsx"],
            key="elasticity_file"
        )

        if uploaded_file is not None:

            try:

                if uploaded_file.name.lower().endswith(".csv"):
                    imported_data = pd.read_csv(uploaded_file)

                else:
                    imported_data = pd.read_excel(uploaded_file)

                st.success("File uploaded successfully.")

                st.write("Imported data preview:")

                st.dataframe(
                    imported_data.head(20),
                    use_container_width=True,
                    hide_index=True
                )

                st.write("Available columns:")

                st.write(list(imported_data.columns))

                st.session_state["imported_elasticity_data"] = imported_data

            except Exception as e:

                st.error(f"Could not read the uploaded file: {e}")

        else:

            st.info(
                "Upload a CSV or Excel file containing historical "
                "selling prices and quantities."
            )


            st.divider()

            st.markdown("""
            <div style="
                background: white;
                border: 1px solid #E5EAF2;
                border-left: 5px solid #1769AA;
                padding: 18px;
                border-radius: 10px;
                margin-bottom: 20px;
            ">
                <h3 style="margin: 0; color: #1769AA;">
                    Elasticity Estimation
                </h3>
                <p style="color: #64748B; margin: 6px 0 0;">
                    Configure your dataset and estimate the relationship
                    between product prices and demand.
                </p>    
            </div>
            """, unsafe_allow_html=True)

    import statsmodels.api as sm

    data_source = st.radio(
        "Choose data for estimation",
        ["Manual Entry", "Imported Historical Data"],
        horizontal=True
    )

    analysis_data = None

    if data_source == "Manual Entry":

        analysis_data = st.session_state.get(
            "custom_elasticity_data"
        )

        if analysis_data is not None:

            analysis_data = analysis_data.rename(columns={
                "Selling Price": "price",
                "Quantity Sold": "quantity",
                "Promotion": "promotion"
            })

    else:

        imported = st.session_state.get(
            "imported_elasticity_data"
        )

        if imported is not None:

            columns = imported.columns.tolist()

            price_column = st.selectbox(
                "Select selling price column",
                columns,
                key="import_price"
            )

            quantity_column = st.selectbox(
                "Select quantity sold column",
                columns,
                key="import_quantity"
            )

            promotion_column = st.selectbox(
                "Select promotion column (optional)",
                ["None"] + columns,
                key="import_promotion"
            )

            analysis_data = pd.DataFrame({
                "price": imported[price_column],
                "quantity": imported[quantity_column]
            })

            if promotion_column != "None":
                analysis_data["promotion"] = imported[
                    promotion_column
                ]

    predict_clicked = st.button(
        "🚀 Predict Elasticity",
        type="primary",
        use_container_width=True
    )

    if predict_clicked and analysis_data is not None:

        required = ["price", "quantity"]

        if all(col in analysis_data.columns for col in required):

            analysis_data = analysis_data.copy()

            analysis_data["price"] = pd.to_numeric(
                analysis_data["price"], errors="coerce"
            )

            analysis_data["quantity"] = pd.to_numeric(
                analysis_data["quantity"], errors="coerce"
            )

            analysis_data = analysis_data.replace(
                [np.inf, -np.inf], np.nan
            ).dropna(subset=["price", "quantity"])

            analysis_data = analysis_data[
                (analysis_data["price"] > 0) &
                (analysis_data["quantity"] > 0)
            ].copy()

            st.write(
                f"Valid observations available: {len(analysis_data)}"
            )

            if len(analysis_data) < 10:

                st.warning(
                    "At least 10 valid observations are required "
                    "for this estimator. More observations are "
                    "recommended for business use."
                )

            elif analysis_data["price"].nunique() < 5:

                st.warning(
                    "At least 5 distinct price levels are required "
                    "to estimate a meaningful price response."
                )

            else:

                analysis_data["log_price"] = np.log(
                    analysis_data["price"]
                )

                analysis_data["log_quantity"] = np.log(
                    analysis_data["quantity"]
                )

                X = analysis_data[["log_price"]].copy()

                if "promotion" in analysis_data.columns:

                    promotion = analysis_data["promotion"]

                    if promotion.dtype == bool:

                        X["promotion"] = promotion.astype(int)

                    else:

                        numeric_promotion = pd.to_numeric(
                            promotion, errors="coerce"
                        )

                        if numeric_promotion.notna().all():

                            X["promotion"] = numeric_promotion

                        else:

                            X["promotion"] = (
                                promotion.astype(str)
                                .str.strip()
                                .str.lower()
                                .isin(["yes", "true", "1", "promotion"])
                                .astype(int)
                            )

                X = sm.add_constant(X)

                y = analysis_data["log_quantity"]

                model = sm.OLS(y, X).fit(cov_type="HC3")

                elasticity = model.params["log_price"]
                p_value = model.pvalues["log_price"]
                std_error = model.bse["log_price"]

                confidence_interval = model.conf_int().loc[
                    "log_price"
                ]

                lower_ci = confidence_interval.iloc[0]
                upper_ci = confidence_interval.iloc[1]

                r_squared = model.rsquared

                st.success("Elasticity estimation completed.")

                st.subheader("Estimation Results")

                c1, c2, c3 = st.columns(3)

                c1.metric(
                    "Price Elasticity",
                    f"{elasticity:.4f}"
                )

                c2.metric(
                    "P-value",
                    f"{p_value:.4g}"
                )

                c3.metric(
                    "R-squared",
                    f"{r_squared:.4f}"
                )

                c4, c5, c6 = st.columns(3)

                c4.metric(
                    "Standard Error",
                    f"{std_error:.4f}"
                )

                c5.metric(
                    "95% CI Lower",
                    f"{lower_ci:.4f}"
                )

                c6.metric(
                    "95% CI Upper",
                    f"{upper_ci:.4f}"
                )

                st.subheader("Business Interpretation")

                if upper_ci < 0:

                    if elasticity < -1:
                        st.info(
                            "The estimated demand response is elastic. "
                            "Quantity is estimated to respond more than "
                            "proportionally to price changes."
                        )

                    else:
                        st.info(
                            "The estimated demand response is inelastic. "
                            "Quantity is estimated to respond less than "
                            "proportionally to price changes."
                        )

                elif lower_ci > 0:

                    st.warning(
                        "The estimated price response is positive. "
                        "Review the data and business context carefully."
                    )

                else:

                    st.warning(
                        "The confidence interval includes zero. "
                        "There is insufficient statistical evidence "
                        "of a clear price response."
                    )

                if p_value >= 0.05:

                    st.warning(
                        "The price coefficient is not statistically "
                        "significant at the 5% level."
                    )

                st.subheader("Historical Demand and Price")

                chart_data = analysis_data[
                    ["price", "quantity"]
                ].sort_values("price")

                st.scatter_chart(
                    chart_data,
                    x="price",
                    y="quantity"
                )

                st.subheader("Price Change Simulation")

                price_change = st.slider(
                    "Proposed price change (%)",
                    min_value=-30,
                    max_value=30,
                    value=5,
                    step=1,
                    key="custom_price_change"
                )

                current_price = analysis_data["price"].mean()

                baseline_quantity = analysis_data["quantity"].mean()

                new_price = current_price * (
                    1 + price_change / 100
                )

                quantity_change = (
                    (1 + price_change / 100) ** elasticity
                ) - 1

                expected_quantity = (
                    baseline_quantity * (1 + quantity_change)
                )

                baseline_revenue = (
                    current_price * baseline_quantity
                )

                projected_revenue = (
                    new_price * expected_quantity
                )

                revenue_change = (
                    projected_revenue - baseline_revenue
                )

                c1, c2, c3 = st.columns(3)

                c1.metric(
                    "Simulated Price",
                    f"{new_price:,.2f}"
                )

                c2.metric(
                    "Expected Quantity",
                    f"{expected_quantity:,.2f}",
                    f"{quantity_change * 100:+.2f}%"
                )

                c3.metric(
                    "Revenue Change",
                    f"{revenue_change:+,.2f}"
                )

                st.warning(
                    "These are model-based estimates, not guaranteed "
                    "outcomes. The regression describes historical "
                    "relationships and does not automatically establish "
                    "a causal price effect. The simulation assumes "
                    "constant elasticity and uses average historical "
                    "price and quantity as its baseline."
                )

                st.session_state["latest_elasticity_model"] = {
    "elasticity": float(elasticity),
    "p_value": float(p_value),
    "std_error": float(std_error),
    "lower_ci": float(lower_ci),
    "upper_ci": float(upper_ci),
    "r_squared": float(r_squared),
    "observations": len(analysis_data),
    "baseline_price": float(analysis_data["price"].mean()),
    "baseline_quantity": float(analysis_data["quantity"].mean()),
    "baseline_revenue": float(
        (analysis_data["price"] * analysis_data["quantity"]).mean()
    ),
    "data": analysis_data.to_dict(orient="records")
}

        else:

            st.error(
                "The data must contain selling price and quantity columns."
            )

    else:

        st.info(
            "Enter manual observations or import historical data "
            "to begin elasticity estimation."
        )
# --------------------------------------------------
# SAVED PREDICTION RESULTS
# --------------------------------------------------

st.divider()

st.header("📊 Prediction Results")

saved_results = st.session_state.get("latest_elasticity_model")

if saved_results is None:

    st.info(
        "No prediction results available yet. "
        "Enter your historical data and click Predict Elasticity."
    )

else:

    st.success("Your latest elasticity prediction is available.")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Price Elasticity",
        f"{saved_results['elasticity']:.4f}"
    )

    c2.metric(
        "P-value",
        f"{saved_results['p_value']:.4g}"
    )

    c3.metric(
        "R-squared",
        f"{saved_results['r_squared']:.4f}"
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "Standard Error",
        f"{saved_results['std_error']:.4f}"
    )

    c5.metric(
        "Lower 95% Confidence Limit",
        f"{saved_results['lower_ci']:.4f}"
    )

    c6.metric(
        "Upper 95% Confidence Limit",
        f"{saved_results['upper_ci']:.4f}"
    )

    st.subheader("Model Information")

    st.write(
        f"Valid observations: {saved_results['observations']}"
    )

    st.write(
        f"Average historical price: "
        f"{saved_results['baseline_price']:.2f}"
    )

    st.write(
        f"Average historical quantity: "
        f"{saved_results['baseline_quantity']:.2f}"
    )

    st.write(
        f"Average observed transaction-period revenue: "
        f"{saved_results['baseline_revenue']:.2f}"
    )

    if saved_results["upper_ci"] < 0:

        if saved_results["elasticity"] < -1:
            st.info("Classification: Elastic demand")

        else:
            st.info("Classification: Inelastic demand")

    else:
        st.warning(
            "Classification: Uncertain price response"
        )

    if saved_results["p_value"] < 0.05:
        st.success("Statistically significant at the 5% level.")
    else:
        st.warning("Not statistically significant at the 5% level.")

    st.subheader("Historical Data Used")

    saved_data = pd.DataFrame(saved_results["data"])

    st.dataframe(
        saved_data,
        use_container_width=True,
        hide_index=True
    )

        # --------------------------------------------------
    # EXPORT CUSTOM ELASTICITY RESULTS
    # --------------------------------------------------

    st.divider()
    st.subheader("📥 Export Estimation Results")

    saved_results = st.session_state.get("latest_elasticity_model")

    if saved_results is not None:

        # Summary results
        summary_data = pd.DataFrame([{
            "Price Elasticity": saved_results["elasticity"],
            "P-value": saved_results["p_value"],
            "Standard Error": saved_results["std_error"],
            "Lower Confidence Interval": saved_results["lower_ci"],
            "Upper Confidence Interval": saved_results["upper_ci"],
            "R-squared": saved_results["r_squared"],
            "Observations": saved_results["observations"],
            "Average Selling Price": saved_results["baseline_price"],
            "Average Quantity Sold": saved_results["baseline_quantity"],
            "Average Period Revenue": saved_results["baseline_revenue"]
        }])

        # Historical observations
        historical_data = pd.DataFrame(saved_results["data"])

        # Pricing simulation
        elasticity = saved_results["elasticity"]
        baseline_price = saved_results["baseline_price"]
        baseline_quantity = saved_results["baseline_quantity"]

        price_changes = [-0.10, -0.05, 0, 0.05, 0.10]

        simulation_rows = []

        baseline_revenue = baseline_price * baseline_quantity

        for change in price_changes:

            new_price = baseline_price * (1 + change)

            new_quantity = baseline_quantity * (
                (1 + change) ** elasticity
            )

            new_revenue = new_price * new_quantity

            simulation_rows.append({
                "Price Change (%)": change * 100,
                "Simulated Price": new_price,
                "Simulated Quantity": new_quantity,
                "Simulated Revenue": new_revenue,
                "Revenue Change": new_revenue - baseline_revenue
            })

        simulation_data = pd.DataFrame(simulation_rows)

        # CSV download
        csv_data = summary_data.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📄 Download Results as CSV",
            data=csv_data,
            file_name="custom_elasticity_results.csv",
            mime="text/csv"
        )

        # Excel download
        excel_buffer = BytesIO()

        with pd.ExcelWriter(
            excel_buffer,
            engine="openpyxl"
        ) as writer:

            summary_data.to_excel(
                writer,
                sheet_name="Elasticity Summary",
                index=False
            )

            historical_data.to_excel(
                writer,
                sheet_name="Historical Data",
                index=False
            )

            simulation_data.to_excel(
                writer,
                sheet_name="Pricing Simulations",
                index=False
            )

        st.download_button(
            label="📊 Download Complete Report as Excel",
            data=excel_buffer.getvalue(),
            file_name="custom_elasticity_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    else:
        st.info("Run an elasticity estimation before exporting results.")
# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Pricing Intelligence System | Analytical decision support | "
    "All pricing actions require management approval."
)
