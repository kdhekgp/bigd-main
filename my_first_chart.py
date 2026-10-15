import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "AppleGothic"  # 윈도우는 Malgun Gothic

temperatures = [16, 13, 7, 7, 12]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(temperatures)
for i, p in enumerate(temperatures):
  ax.annotate(f"{p:,}", (i, p), textcoords="offset points", xytext=(0, 8), ha="center")

ax.set_title("요즘 최저 온도")
fig.savefig("my_first_chart.png")