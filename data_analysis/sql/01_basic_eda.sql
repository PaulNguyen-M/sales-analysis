-- 💰 Revenue by product
SELECT Hang, SUM(Doanh_Thu) AS total_revenue
FROM sales
GROUP BY Hang
ORDER BY total_revenue DESC;

-- 📦 Total quantity sold
SELECT SUM(SL_Xuat) AS total_quantity
FROM sales;