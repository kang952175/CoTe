select BOARD_ID, WRITER_ID, TITLE, PRICE, 
    case 
    when status = 'sale' then '판매중'
    when status = 'reserved' then '예약중'
    when status = 'done' then '거래완료'
    end as STATUS
from used_goods_board
where date_format(CREATED_DATE, '%Y-%m-%d') = '2022-10-05'
order by BOARD_ID desc