"""empty message

Revision ID: dd4a73113bc6
Revises: d39f83f51f4e
Create Date: 2020-10-20 21:18:45.325815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd4a73113bc6'
down_revision = 'd39f83f51f4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_transicao_grp_valida',
    sa.Column('id_transicao_grp', sa.Integer(), nullable=False),
    sa.Column('id_grupo', sa.Integer(), nullable=False),
    sa.Column('id_evento', sa.Integer(), nullable=True),
    sa.Column('id_situacao_destino', sa.Integer(), nullable=False),
    sa.Column('ind_consistente', sa.String(length=1), nullable=False),
    sa.Column('ind_efetiva', sa.String(length=1), nullable=False),
    sa.Column('sg_tribunal', sa.String(length=30), nullable=False),
    sa.Column('sg_grau', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['id_evento'], ['tb_desc_evento.id_evento'], ),
    sa.ForeignKeyConstraint(['id_grupo'], ['tb_desc_grp_situacao.id_grupo'], ),
    sa.ForeignKeyConstraint(['id_situacao_destino'], ['tb_desc_situacao.id_situacao'], ),
    sa.PrimaryKeyConstraint('id_transicao_grp')
    )
    op.create_table('tb_transicao_valida',
    sa.Column('id_transicao', sa.Integer(), nullable=False),
    sa.Column('id_situacao_origem', sa.Integer(), nullable=False),
    sa.Column('id_evento', sa.Integer(), nullable=True),
    sa.Column('id_situacao_destino', sa.Integer(), nullable=False),
    sa.Column('ind_consistente', sa.String(length=1), nullable=False),
    sa.Column('ind_efetiva', sa.String(length=1), nullable=False),
    sa.Column('sg_tribunal', sa.String(length=30), nullable=False),
    sa.Column('sg_grau', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['id_evento'], ['tb_desc_evento.id_evento'], ),
    sa.ForeignKeyConstraint(['id_situacao_destino'], ['tb_desc_situacao.id_situacao'], ),
    sa.ForeignKeyConstraint(['id_situacao_origem'], ['tb_desc_situacao.id_situacao'], ),
    sa.PrimaryKeyConstraint('id_transicao')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_transicao_valida')
    op.drop_table('tb_transicao_grp_valida')
    # ### end Alembic commands ###