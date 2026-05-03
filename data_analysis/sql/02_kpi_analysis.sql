-- 💰 Revenue & Profit
SELECT 
    Hang,
    SUM(Doanh_Thu) AS revenue,
    SUM(Doanh_Thu - Tien_Nhap) AS profit
FROM sales
GROUP BY Hang
ORDER BY profit DESC;