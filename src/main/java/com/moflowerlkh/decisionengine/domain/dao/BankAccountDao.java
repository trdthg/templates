package com.moflowerlkh.decisionengine.domain.dao;

import com.moflowerlkh.decisionengine.domain.entities.BankAccount;
import com.moflowerlkh.decisionengine.domain.entities.activities.DepositActivity;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface BankAccountDao extends JpaRepository<BankAccount, Long> {
    public List<BankAccount> findByUserID(Long userId);
}