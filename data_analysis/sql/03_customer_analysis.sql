-- 👥 Top customers
SELECT 
    Khach_Hang,
    SUM(Doanh_Thu) AS total_revenue
FROM sales
GROUP BY Khach_Hang
ORDER BY total_revenue DESC;

-- 🎯 Customer segmentation (simple)
SELECT 
    Khach_Hang,
    COUNT(*) AS num_transactions,
    SUM(Doanh_Thu) AS total_revenue
FROM sales
GROUP BY Khach_Hang;