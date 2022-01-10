package com.moflowerlkh.decisionengine.model;

import lombok.Data;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Data
@Table(name = "shopping_goods_tb")
public class ShoppingGoods {
    @Id
    @Column(name = "id", nullable = false)
    private Long id;

    @Column(nullable = false)
    private String info;

    // 商品总数
    @Column(nullable = false)
    private long goodsTotal;

}
