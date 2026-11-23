
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Pricing Intelligence System",
    page_icon="📊",
    layout="wide"
)

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
profitability = load_data("profitability_portfolio.csv")
increase_scenarios = load_data("all_product_simulations.csv")
reduction_scenarios = load_data("price_reduction_results.csv")


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("📊 Pricing Intelligence")
st.sidebar.caption("Customer & Product Pricing Decision Support")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Overview",
        "Product Intelligence",
        "Customer Segments",
        "Pricing Simulator",
        "Profitability Analysis"
    ]
)

st.sidebar.divider()
st.sidebar.info(
    "This system provides analytical pricing recommendations. "
    "All proposed price changes require business review and approval."
)


# --------------------------------------------------
# EXECUTIVE OVERVIEW
# --------------------------------------------------

if page == "Executive Overview":

    st.title("Executive Overview")
    st.caption("Retail pricing performance and opportunity summary")

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

    c1, c2, c3 = st.columns(3)

    c1.metric("Products Analysed", f"{total_products:,}")
    c2.metric(
        "Potential Revenue (5% Scenario)",
        f"{potential_revenue:,.2f}"
    )
    c3.metric("Average Price Elasticity", f"{avg_elasticity:.3f}")

    c4, c5, c6 = st.columns(3)

    c4.metric("Proposed 5% Tests", int(five_pct))
    c5.metric("Proposed 3% Tests", int(three_pct))
    c6.metric("Products Awaiting Cost Data", int(cost_pending))

    st.divider()

    st.subheader("Top Pricing Opportunities")

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

    st.subheader("Important Business Considerations")

    st.warning(
        "The revenue figures are model-based scenarios, not guaranteed "
        "results. They are not profit estimates. Actual costs, competitor "
        "reactions, inventory and customer behaviour must be considered "
        "before approving a price change."
    )


# --------------------------------------------------
# PRODUCT INTELLIGENCE
# --------------------------------------------------

elif page == "Product Intelligence":

    st.title("Product Intelligence")
    st.caption("Product-level price sensitivity and commercial opportunities")

    departments = sorted(
        products["DEPARTMENT"].dropna().unique()
    )

    selected_department = st.selectbox(
        "Filter by department",
        ["All Departments"] + departments
    )

    filtered = products.copy()

    if selected_department != "All Departments":
        filtered = filtered[
            filtered["DEPARTMENT"] == selected_department
        ]

    st.metric("Products in View", len(filtered))

    st.subheader("Product Elasticity Results")

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

    st.subheader("Price Elasticity Comparison")

    chart_data = (
        filtered[["COMMODITY_DESC", "elasticity"]]
        .dropna()
        .set_index("COMMODITY_DESC")
    )

    st.bar_chart(chart_data)

    st.caption(
        "More negative elasticity indicates greater estimated "
        "demand sensitivity to price."
    )


# --------------------------------------------------
# CUSTOMER SEGMENTS
# --------------------------------------------------

elif page == "Customer Segments":

    st.title("Customer Segment Intelligence")

    st.caption(
        "Department-level price sensitivity across household income groups"
    )

    department_options = sorted(
        segments["DEPARTMENT"].dropna().unique()
    )

    selected_department = st.selectbox(
        "Select department",
        department_options
    )

    segment_view = segments[
        segments["DEPARTMENT"] == selected_department
    ].copy()

    st.metric(
        "Income Groups with Estimates",
        len(segment_view)
    )

    st.subheader("Income Group Elasticity")

    if "INCOME_DESC" in segment_view.columns:

        chart = (
            segment_view[["INCOME_DESC", "elasticity"]]
            .dropna()
            .set_index("INCOME_DESC")
        )

        st.bar_chart(chart)

    st.subheader("Detailed Segment Estimates")

    st.dataframe(
        segment_view,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "These are department-level income-segment estimates. "
        "They are not product-specific household elasticities. "
        "Use them to guide broad promotions, assortment and value "
        "strategies rather than individualized income-based pricing."
    )


# --------------------------------------------------
# PRICING SIMULATOR
# --------------------------------------------------

elif page == "Pricing Simulator":

    st.title("Pricing Simulator")

    st.caption(
        "Explore the estimated revenue effect of changing a product's price"
    )

    product_options = products[
        ["PRODUCT_ID", "COMMODITY_DESC"]
    ].drop_duplicates()

    product_options["label"] = (
        product_options["COMMODITY_DESC"].astype(str)
        + " | ID: "
        + product_options["PRODUCT_ID"].astype(str)
    )

    selected_label = st.selectbox(
        "Choose a product",
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

    st.subheader("Current Product Baseline")

    c1, c2, c3 = st.columns(3)

    c1.metric("Estimated Average Price", f"{current_price:.2f}")
    c2.metric("Baseline Quantity", f"{baseline_quantity:,.0f}")
    c3.metric("Price Elasticity", f"{elasticity:.3f}")

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

    st.divider()

    st.subheader("Simulation Results")

    c1, c2, c3 = st.columns(3)

    c1.metric("New Price", f"{new_price:.2f}")

    c2.metric(
        "Expected Quantity",
        f"{expected_quantity:,.2f}",
        f"{quantity_change * 100:.2f}%"
    )

    c3.metric(
        "Projected Revenue",
        f"{projected_revenue:,.2f}",
        f"{revenue_change_pct:.2f}%"
    )

    st.metric(
        "Estimated Revenue Change",
        f"{revenue_change:+,.2f}"
    )

    st.warning(
        "This simulation assumes constant price elasticity and "
        "does not account for costs, competitors, stock availability "
        "or changes in customer behaviour. It is not a profit forecast."
    )


# --------------------------------------------------
# PROFITABILITY ANALYSIS
# --------------------------------------------------

elif page == "Profitability Analysis":

    st.title("Profitability Analysis")

    st.caption(
        "Gross-profit evaluation using actual retailer cost and price data"
    )

    st.subheader("Product Cost Data Status")

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

    c1, c2, c3 = st.columns(3)

    c1.metric("Products Analysed", len(profitability))
    c2.metric("Products with Cost Data", ready)
    c3.metric("Products Awaiting Cost Data", pending)

    st.subheader("Product Cost Information")

    st.dataframe(
        profitability,
        use_container_width=True,
        hide_index=True
    )

    if ready == 0:

        st.warning(
            "Actual product costs and current selling prices have not "
            "been supplied. Therefore, reliable gross-profit simulations "
            "cannot yet be calculated."
        )

    st.info(
        "Upload the completed product profitability input template "
        "when the retailer provides actual unit costs and selling prices."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Pricing Intelligence System | Analytical decision support | "
    "All pricing actions require management approval."
)
