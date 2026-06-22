"""
클래식 스탯 vs 세이버메트릭스 - 팀 득점 설명력 분석
데이터: mlb_team_batting.csv (MLB 2021-2024, 120 팀-시즌)
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("mlb_team_batting.csv")
classic = ['BA','H','HR']      # 클래식 지표
saber   = ['OPS','OPS_plus']   # 세이버 지표
target  = 'R'                  # 팀 득점

# --- 상관분석 ---
corr = df[classic+saber+[target]].corr()[target].drop(target).sort_values(ascending=False)
print("각 지표와 팀 득점(R)의 상관계수")
for m,c in corr.items():
    print(f"  {'[세이버]' if m in saber else '[클래식]'} {m:9s}: {c:.3f}")
print(f"\n클래식 평균: {corr[classic].mean():.3f}  |  세이버 평균: {corr[saber].mean():.3f}")

# --- 시각화: 상관 막대그래프 ---
sns.set_style("whitegrid")
c2 = corr.sort_values()
colors = ['#d62728' if m in saber else '#1f77b4' for m in c2.index]
plt.figure(figsize=(8,5))
plt.barh(c2.index, c2.values, color=colors)
plt.xlabel('Correlation with Team Runs'); plt.xlim(0,1)
plt.title('Which Stat Best Explains Team Scoring?')
plt.tight_layout(); plt.savefig('fig_correlation.png', dpi=120)
print("\n그래프 저장: fig_correlation.png")
