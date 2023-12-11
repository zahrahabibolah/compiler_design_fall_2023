// Generated from C:/Users/black/compiler_design_fall_2023/HW2/main.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link mainParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface mainVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link mainParser#equation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEquation(mainParser.EquationContext ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(mainParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#multiplyingExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplyingExpression(mainParser.MultiplyingExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#powExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPowExpression(mainParser.PowExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#signedAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSignedAtom(mainParser.SignedAtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(mainParser.AtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#scientific}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitScientific(mainParser.ScientificContext ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#constant}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstant(mainParser.ConstantContext ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable(mainParser.VariableContext ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#func_}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc_(mainParser.Func_Context ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#funcname}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncname(mainParser.FuncnameContext ctx);
	/**
	 * Visit a parse tree produced by {@link mainParser#relop}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelop(mainParser.RelopContext ctx);
}