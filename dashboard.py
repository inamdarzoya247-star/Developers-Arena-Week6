import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# =========================================================
# SETUP
# =========================================================

os.makedirs("visualizations", exist_ok=True)

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Seaborn style
sns.set_theme(style="whitegrid")

print("=" * 60)
print("          INTERACTIVE SALES DASHBOARD")
print("=" * 60)

print("\nDataset loaded successfully!")
print("Dataset shape:", df.shape)


# =========================================================
# 1. BAR CHART - PRODUCT-WISE SALES
# =========================================================

product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=product_sales.index,
    y=product_sales.values
)

plt.title("Product-wise Total Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "visualizations/product_sales_seaborn.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Bar chart created successfully!")


# =========================================================
# 2. BOX PLOT - SALES DISTRIBUTION
# =========================================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    x="Product",
    y="Total_Sales",
    data=df
)

plt.title("Sales Distribution by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "visualizations/sales_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Box plot created successfully!")


# =========================================================
# 3. VIOLIN PLOT - QUANTITY DISTRIBUTION
# =========================================================

plt.figure(figsize=(10, 6))

sns.violinplot(
    x="Product",
    y="Quantity",
    data=df
)

plt.title("Quantity Distribution by Product")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "visualizations/sales_violinplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Violin plot created successfully!")


# =========================================================
# 4. CORRELATION HEATMAP
# =========================================================

numeric_df = df.select_dtypes(include="number")

correlation = numeric_df.corr()

plt.figure(figsize=(10, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig(
    "visualizations/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Correlation heatmap created successfully!")


# =========================================================
# 5. SALES TREND LINE CHART
# =========================================================

daily_sales = (
    df.groupby("Date")["Total_Sales"]
    .sum()
)

plt.figure(figsize=(12, 6))

sns.lineplot(
    x=daily_sales.index,
    y=daily_sales.values,
    marker="o"
)

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "visualizations/sales_trend_line.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Sales trend line chart created successfully!")


# =========================================================
# 6. 2x2 DASHBOARD
# =========================================================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(16, 12)
)

# ---- Chart 1: Product Sales ----

sns.barplot(
    x=product_sales.index,
    y=product_sales.values,
    ax=axes[0, 0]
)

axes[0, 0].set_title("Product-wise Total Sales")
axes[0, 0].set_xlabel("Product")
axes[0, 0].set_ylabel("Total Sales")
axes[0, 0].tick_params(
    axis="x",
    rotation=45
)


# ---- Chart 2: Sales Distribution ----

sns.boxplot(
    x="Product",
    y="Total_Sales",
    data=df,
    ax=axes[0, 1]
)

axes[0, 1].set_title("Sales Distribution by Product")
axes[0, 1].set_xlabel("Product")
axes[0, 1].set_ylabel("Total Sales")
axes[0, 1].tick_params(
    axis="x",
    rotation=45
)


# ---- Chart 3: Quantity Distribution ----

sns.violinplot(
    x="Product",
    y="Quantity",
    data=df,
    ax=axes[1, 0]
)

axes[1, 0].set_title("Quantity Distribution by Product")
axes[1, 0].set_xlabel("Product")
axes[1, 0].set_ylabel("Quantity")
axes[1, 0].tick_params(
    axis="x",
    rotation=45
)


# ---- Chart 4: Daily Sales Trend ----

sns.lineplot(
    x=daily_sales.index,
    y=daily_sales.values,
    ax=axes[1, 1],
    marker="o"
)

axes[1, 1].set_title("Daily Sales Trend")
axes[1, 1].set_xlabel("Date")
axes[1, 1].set_ylabel("Total Sales")
axes[1, 1].tick_params(
    axis="x",
    rotation=45
)


# Dashboard title

fig.suptitle(
    "Sales Dashboard - Statistical Overview",
    fontsize=18
)

plt.tight_layout()

plt.savefig(
    "visualizations/sales_dashboard_2x2.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("2x2 dashboard created successfully!")


# =========================================================
# 7. INTERACTIVE PLOTLY CHART
# =========================================================

fig = px.scatter(
    df,
    x="Price",
    y="Total_Sales",
    color="Product",
    hover_data=[
        "Date",
        "Quantity",
        "Region",
        "Customer_ID"
    ],
    title="Interactive Price vs Total Sales"
)

fig.update_layout(
    xaxis_title="Price",
    yaxis_title="Total Sales"
)

# Save interactive chart

fig.write_html(
    "visualizations/interactive_sales_chart.html"
)

print("Interactive Plotly chart created successfully!")


# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n" + "=" * 60)
print("ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
print("=" * 60)