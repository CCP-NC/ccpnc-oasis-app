from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    SearchQuantities,
    Axis,
    Menu,
    MenuItemTerms,
    MenuItemPeriodicTable,
    MenuItemHistogram
)

app_entry_point = AppEntryPoint(
    name='NewApp',
    description='New app entry point configuration.',
    app=App(
        label='NEW NMR APP',
        path='app',
        category='simulation',
        # Load search quantities from custom schema first
        search_quantities=SearchQuantities(
            include=[
                '*#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                '*#nomad_simulations.schema_packages.model_system.ModelSystem',
                '*#nomad_simulations.schema_packages.atoms_state.AtomsState',
                '*#nomad_simulations.schema_packages.general.Program',
            ]
        ),
        # Add filters to ensure only entries with custom schema are shown
        filters_locked={
            'section_defs.definition_qualified_name': [
                'nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation'
            ]
        },
        columns=[
            Column(
                quantity='data.ccpnc_metadata.material_properties.chemical_name#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                label='Chemical Name',
                selected=True,
            ),
            Column(
                quantity='data.ccpnc_metadata.ccpnc_record.immutable_id#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                label='Magres Immutable ID',
                selected=True,
            ),
            Column(
                quantity='upload_create_time',
                label='Upload Time',
                selected=True,
            ),
            Column(
                quantity='main_author.name',
                label='Main Author',
                selected=True,
            )
        ],
        menu=Menu(
            title='NMR Filters',
            size='sm',
            items=[
                # Material properties submenu
                Menu(
                    title='Material Properties',
                    size='md',
                    items=[
                        MenuItemTerms(
                            quantity='data.ccpnc_metadata.material_properties.chemical_name#nomad_oasis_schema_parser_plugin.schema_packages.schema_package.CCPNCSimulation',
                            options=10,
                            width=12,
                        ),
                    ],
                ),
                Menu(
                    title='DFT Code',
                    size='md',
                    items=[
                        MenuItemTerms(
                            quantity='data.program.name#nomad_simulations.schema_packages.general.Program',
                            # quantity='nomad_simulations.schema_packages.general.Program.name',
                            options=10,
                            width=12,
                        ),
                        MenuItemHistogram(x=Axis(search_quantity='data.program.version#nomad_simulations.schema_packages.general.Program')),
                    ],
                ),
            ],
        )
    ),
)
