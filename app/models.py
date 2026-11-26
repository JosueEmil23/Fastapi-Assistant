from datetime import date, datetime
from decimal import Decimal
from sqlalchemy import Date, DateTime, ForeignKey, Integer, Numeric, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    account_type: Mapped[str] = mapped_column(String(40), default= "cash", nullable=False)
    currency: Mapped[str] = mapped_column(String(10), default="PEN", nullable=False)
    initial_balance: Mapped[Decimal] = mapped_column(Numeric(12,2), default=Decimal("0.00"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    transactions:Mapped[list["Transaction"]] = relationship(
        back_populates="account", cascade="all, delete-orphan"
    )

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    kind:Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    transactions: Mapped[list["Transaction"]] = relationship(back_populates="category", cascade="all, delete-orphan")

class Transaction(Base):
    __tablename__= "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False, index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("accounts.id", ondelete="RESTRICT"), nullable=False, index=True)
    amount: Mapped[Decimal] =mapped_column(Numeric(12, 2), nullable=False)
    tx_type: Mapped[str] = mapped_column(String(20), default="", nullable=False)
    description: Mapped[str] = mapped_column(String(255), default="", nullable=False)
    tx_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    account: Mapped["Account"] = relationship(back_populates="transactions")
    category: Mapped["Category"] = relationship(back_populates="transactions")

class Budget(Base):
    __tablename__ ="budgets"
    __table_args__ = (
        UniqueConstraint("category_id", "year", "month", name="uq_budget_category_period"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"), nullable=False, index=True
    )
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    month: Mapped[int] = mapped_column(Integer, nullable=False)
    limit_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    category: Mapped["Category"] = relationship(back_populates="budgets")


